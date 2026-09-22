"""
Rewrite the `categories:` block of the blog markdown files so they match the
controlled vocabulary in researchapp/category_vocabulary.py.

Same shape as tags_apply: markdown is the source of truth, the files are
edited in place, and only the categories block is touched.

BLOGS_ROOT is a git repo, so review with `git -C "$BLOGS_ROOT" diff` and undo
with `git -C "$BLOGS_ROOT" checkout .` if you don't like the result.

Usage:
    python manage.py categories_apply              # dry run: diff + summary
    python manage.py categories_apply --summary    # dry run: summary only
    python manage.py categories_apply --apply      # actually write the files
"""

import os
from collections import Counter

from django.core.management.base import BaseCommand, CommandError

from researchapp.category_vocabulary import CATEGORIES, POST_CATEGORIES, RENAMES
from researchapp.frontmatter import read_list, render_list, split_frontmatter

from settings import BLOGS_ROOT


def map_categories(filename, current):
    """Work out the categories a post should end up with.

    POST_CATEGORIES is the authority where it has an entry - those are the
    hand-made routing decisions. Everything else just gets the renames, so a
    post written after the consolidation is handled sensibly without needing
    a line in the mapping.
    """
    if filename in POST_CATEGORIES:
        return sorted(POST_CATEGORIES[filename])
    return sorted({RENAMES.get(c, c) for c in current})


class Command(BaseCommand):
    help = "Rewrite blog markdown categories to match the controlled vocabulary. Dry-run by default."

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

    def handle(self, *args, **options):
        changes = []
        before = Counter()
        after = Counter()
        unknown = Counter()
        no_block = []
        orphaned = []

        seen_files = set()

        for filename in sorted(os.listdir(BLOGS_ROOT)):
            if not filename.endswith(".md"):
                continue
            seen_files.add(filename)

            path = os.path.join(BLOGS_ROOT, filename)
            with open(path) as f:
                lines = f.readlines()

            block = split_frontmatter(lines, "categories")
            if block is None:
                no_block.append(filename)
                continue

            old = read_list(lines, block)
            new = map_categories(filename, old)

            for c in old:
                before[c] += 1
            for c in new:
                after[c] += 1
                if c not in CATEGORIES:
                    unknown[c] += 1
            if old and not new:
                orphaned.append(filename)

            start, end = block
            rendered = render_list(new, lines[start])
            if lines[start:end] != rendered:
                changes.append((filename, old, new, lines, block))

        stale = sorted(set(POST_CATEGORIES) - seen_files)
        if stale:
            raise CommandError(
                "POST_CATEGORIES names files that do not exist in BLOGS_ROOT "
                f"(renamed or deleted posts?): {stale}"
            )

        if unknown:
            self.stdout.write(self.style.ERROR(
                "\nThese categories would survive but are not in CATEGORIES:"
            ))
            for c, n in unknown.most_common():
                self.stdout.write(f"    {n:4d}  {c}")
            raise CommandError("Refusing to continue. Fix category_vocabulary.py.")

        if orphaned:
            raise CommandError(
                f"These posts would end up with no category at all: {orphaned}"
            )

        if not options["summary"]:
            for filename, old, new, _, _ in changes:
                self.stdout.write(f"\n{filename}")
                self.stdout.write(f"  - {sorted(old)}")
                self.stdout.write(f"  + {new}")

        self.print_summary(before, after, changes, no_block)

        if options["apply"]:
            for filename, _, new, lines, block in changes:
                start, end = block
                new_lines = (
                    lines[:start] + render_list(new, lines[start]) + lines[end:]
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
            self.stdout.write(self.style.WARNING("Then run: tools/blogs-reindex --force"))
        else:
            self.stdout.write(self.style.WARNING(
                "\nDRY RUN - nothing written. Re-run with --apply to commit these changes."
            ))

    # ------------------------------------------------------------------ #

    def print_summary(self, before, after, changes, no_block):
        self.stdout.write("")
        self.stdout.write(self.style.MIGRATE_HEADING("=== SUMMARY ==="))
        self.stdout.write(f"  files changed             : {len(changes)}")
        self.stdout.write(f"  files with no categories  : {len(no_block)}")

        self.stdout.write("\n  before:")
        for c, n in before.most_common():
            self.stdout.write(f"    {n:4d}  {c}")
        self.stdout.write("\n  after:")
        for c, n in after.most_common():
            delta = n - before.get(c, 0)
            sign = f"  ({delta:+d})" if delta else ""
            self.stdout.write(f"    {n:4d}  {c}{sign}")
