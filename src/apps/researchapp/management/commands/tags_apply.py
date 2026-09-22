"""
Rewrite the `tags:` block of every blog markdown file so it conforms to the
controlled vocabulary in researchapp/tag_vocabulary.py.

Markdown is the source of truth for tags (see TAGS_PLAN.md), so this command
edits the files in BLOGS_ROOT in place. Only the tags block is touched - the
rest of the frontmatter and the body are copied through byte for byte.

BLOGS_ROOT is a git repo, so review with `git -C "$BLOGS_ROOT" diff` and undo
with `git -C "$BLOGS_ROOT" checkout .` if you don't like the result.

Usage:
    python manage.py tags_apply                 # dry run: per-file diff + summary
    python manage.py tags_apply --summary       # dry run: summary only
    python manage.py tags_apply --apply         # actually write the files
"""

import os
from collections import Counter

from django.core.management.base import BaseCommand, CommandError

from researchapp.tag_vocabulary import ALIASES, DROP, VOCABULARY

from settings import BLOGS_ROOT


def map_tags(tags):
    """Apply ALIASES, remove DROP, de-duplicate, sort.

    Aliases are resolved transitively (a -> b -> c) so the vocabulary file can
    stay readable without every entry having to name the final canonical form.
    """
    out = []
    for tag in tags:
        seen = set()
        while tag in ALIASES and tag not in seen:
            seen.add(tag)
            tag = ALIASES[tag]
        if tag in DROP:
            continue
        if tag not in out:
            out.append(tag)
    return sorted(out)


def split_frontmatter(lines):
    """Return (before, tag_block_slice, after) for the tags: block.

    tag_block_slice is a (start, end) pair of line indexes covering the
    `tags:` line and its `- "..."` items, or None if the post has no tags
    block at all.
    """
    # locate the frontmatter fences
    fences = [i for i, l in enumerate(lines) if l.rstrip("\n") == "---"]
    if len(fences) < 2:
        return None
    head_start, head_end = fences[0], fences[1]

    for i in range(head_start + 1, head_end):
        line = lines[i]
        if line.startswith("tags:") and not line[len("tags:"):].strip():
            end = i + 1
            while end < head_end and lines[end].strip().startswith("-"):
                end += 1
            return (i, end)
    return None


def read_tags(lines, block):
    start, end = block
    return [
        lines[i].replace("- ", "", 1).strip().strip('"').lower()
        for i in range(start + 1, end)
    ]


TAG_INDENT = "  "


def render_tags(tags, header="tags: \n"):
    """Render the tags block, preserving the file's own `tags:` header line.

    Items are indented with TAG_INDENT to match the `categories:` block that
    sits right above them in every post - the markdown parser accepts any
    indentation, but a gratuitous reformat makes the git diff unreadable.
    """
    if not tags:
        return []
    return [header] + [f'{TAG_INDENT}- "{t}"\n' for t in tags]


class Command(BaseCommand):
    help = "Rewrite blog markdown tags to match the controlled vocabulary. Dry-run by default."

    def add_arguments(self, parser):
        parser.add_argument(
            "--apply",
            action="store_true",
            help="Actually write the files. Without this, only a diff is printed.",
        )
        parser.add_argument(
            "--summary",
            action="store_true",
            help="Skip the per-file diff, print only the before/after summary.",
        )
        parser.add_argument(
            "--allow-unknown",
            action="store_true",
            help="Proceed even if a resulting tag is not in VOCABULARY.",
        )

    def handle(self, *args, **options):
        apply_changes = options["apply"]

        changes = []        # (filename, old_tags, new_tags, lines, block)
        before = Counter()
        after = Counter()
        unknown = Counter()
        untouched = 0

        for filename in sorted(os.listdir(BLOGS_ROOT)):
            if not filename.endswith(".md"):
                continue

            path = os.path.join(BLOGS_ROOT, filename)
            with open(path) as f:
                lines = f.readlines()

            block = split_frontmatter(lines)
            if block is None:
                untouched += 1
                continue

            old_tags = read_tags(lines, block)
            new_tags = map_tags(old_tags)

            for t in old_tags:
                before[t] += 1
            for t in new_tags:
                after[t] += 1
                if t not in VOCABULARY:
                    unknown[t] += 1

            # Compare the rendered block against what's actually in the file,
            # not just the tag lists: that way a post whose tags are already
            # canonical but whose formatting has drifted gets repaired too,
            # and re-running the command is a no-op once everything converges.
            start, end = block
            rendered = render_tags(new_tags, header=lines[start])
            if lines[start:end] != rendered:
                changes.append((filename, old_tags, new_tags, lines, block))

        if unknown and not options["allow_unknown"]:
            self.stdout.write(self.style.ERROR(
                "\nThese tags would survive the rewrite but are not in VOCABULARY:"
            ))
            for t, c in unknown.most_common():
                self.stdout.write(f"    {c:4d}  {t}")
            raise CommandError(
                "Refusing to continue. Add them to VOCABULARY, ALIASES or DROP "
                "- or re-run with --allow-unknown."
            )

        if not options["summary"]:
            self.print_diff(changes)

        self.print_summary(before, after, changes, untouched)

        if apply_changes:
            for filename, _, new_tags, lines, block in changes:
                start, end = block
                new_lines = (
                    lines[:start]
                    + render_tags(new_tags, header=lines[start])
                    + lines[end:]
                )
                with open(os.path.join(BLOGS_ROOT, filename), "w") as f:
                    f.writelines(new_lines)
            self.stdout.write(self.style.SUCCESS(
                f"\nApplied to {len(changes)} files in {BLOGS_ROOT}"
            ))
            self.stdout.write(
                'Review with: git -C "$BLOGS_ROOT" diff   |   '
                'Undo with: git -C "$BLOGS_ROOT" checkout .'
            )
            self.stdout.write(self.style.WARNING(
                "Then run: tools/blogs-reindex --force"
            ))
        else:
            self.stdout.write(self.style.WARNING(
                "\nDRY RUN - nothing written. Re-run with --apply to commit these changes."
            ))

    # ------------------------------------------------------------------ #

    def print_diff(self, changes):
        for filename, old_tags, new_tags, _, _ in changes:
            self.stdout.write(f"\n{filename}")
            self.stdout.write(f"  - {sorted(old_tags)}")
            self.stdout.write(f"  + {new_tags}")

    def print_summary(self, before, after, changes, untouched):
        self.stdout.write("")
        self.stdout.write(self.style.MIGRATE_HEADING("=== SUMMARY ==="))
        self.stdout.write(f"  files changed        : {len(changes)}")
        self.stdout.write(f"  files with no tags block: {untouched}")
        self.stdout.write(f"  distinct tags before : {len(before)}")
        self.stdout.write(f"  distinct tags after  : {len(after)}")

        thin = sorted((c, t) for t, c in after.items() if c < 3)
        if thin:
            self.stdout.write(
                f"\n  {len(thin)} surviving tags still used fewer than 3 times "
                "(candidates for another ALIASES/DROP pass):"
            )
            self.stdout.write("  " + ", ".join(f"{t}({c})" for c, t in thin))

        self.stdout.write("\n  resulting vocabulary, by facet:")
        by_facet = {}
        for tag, count in after.items():
            by_facet.setdefault(VOCABULARY.get(tag, "?"), []).append((count, tag))
        for facet in ("domain", "tech", "format", "topic", "?"):
            if facet not in by_facet:
                continue
            items = sorted(by_facet[facet], reverse=True)
            self.stdout.write(f"\n    [{facet}] {len(items)} tags")
            self.stdout.write(
                "      " + ", ".join(f"{t}({c})" for c, t in items)
            )
