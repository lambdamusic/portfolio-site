"""
Read-only health check on the blog tag vocabulary.

Reads the markdown folder directly (NOT the DB) so it can be run before a
reindex, and re-run after every consolidation round to see where things stand.

Markdown is the source of truth for tags - see TAGS_PLAN.md.

Usage:
    python manage.py tags_audit                  # full report
    python manage.py tags_audit --csv out.csv    # also dump tag,count,facet,posts
    python manage.py tags_audit --threshold 3    # cut-line simulation (default 3)
"""

import csv
import os
import re
from collections import Counter, defaultdict

from django.core.management.base import BaseCommand

from researchapp.models import Project, Tag
from researchapp.management.commands.do_blogs_reindex import parse_markdown

from settings import BLOGS_ROOT


try:
    from researchapp.tag_vocabulary import ALIASES, DROP, VOCABULARY
except ImportError:
    # Phase 2 of TAGS_PLAN.md hasn't landed yet - the audit still works,
    # it just can't report on vocabulary conformance.
    ALIASES, DROP, VOCABULARY = {}, set(), {}


def normalize(tag):
    """Fold a tag to a comparison key, so spelling variants collide.

    digital-humanities / digitalhumanities -> digitalhumanitie(s stripped)
    books / book                           -> book
    """
    key = tag.replace("-", "").replace("_", "")
    if key.endswith("ies"):
        key = key[:-3] + "y"
    elif key.endswith("s") and not key.endswith("ss"):
        key = key[:-1]
    return key


def read_posts():
    """Return {filename: (tags, categories)} for every post in BLOGS_ROOT."""
    posts = {}
    for filename in sorted(os.listdir(BLOGS_ROOT)):
        if not filename.endswith(".md"):
            continue
        _, _, _, cats, tags, _ = parse_markdown(os.path.join(BLOGS_ROOT, filename))
        posts[filename] = (tags, cats)
    return posts


class Command(BaseCommand):
    help = "Report on the state of the blog tag vocabulary. Read-only."

    def add_arguments(self, parser):
        parser.add_argument(
            "--csv",
            dest="csv_path",
            help="Write tag,count,facet,posts to this file (for spreadsheet curation).",
        )
        parser.add_argument(
            "--threshold",
            type=int,
            default=3,
            help="Cut-line used for the 'low frequency' section (default 3).",
        )

    def handle(self, *args, **options):
        posts = read_posts()

        tags = Counter()
        cats = Counter()
        tag_to_posts = defaultdict(list)
        for filename, (post_tags, post_cats) in posts.items():
            for t in post_tags:
                tags[t] += 1
                tag_to_posts[t].append(filename)
            for c in post_cats:
                cats[c] += 1

        self.report_summary(posts, tags, cats)
        self.report_duplicates(tags)
        self.report_cut_line(posts, tags, options["threshold"])
        self.report_untagged(posts)
        self.report_projects(tags)
        if VOCABULARY:
            self.report_conformance(tags)

        if options["csv_path"]:
            self.write_csv(options["csv_path"], tags, tag_to_posts)

    # ------------------------------------------------------------------ #

    def h(self, text):
        self.stdout.write("")
        self.stdout.write(self.style.MIGRATE_HEADING(f"=== {text} ==="))

    def report_summary(self, posts, tags, cats):
        self.h("SUMMARY")
        self.stdout.write(f"posts             : {len(posts)}")
        self.stdout.write(f"distinct tags     : {len(tags)}")
        self.stdout.write(f"distinct categories: {len(cats)}")
        self.stdout.write("")
        self.stdout.write("categories:")
        for name, count in cats.most_common():
            self.stdout.write(f"  {count:4d}  {name}")

        self.stdout.write("")
        self.stdout.write("tag frequency distribution:")
        dist = Counter(tags.values())
        for n in sorted(dist):
            self.stdout.write(f"  used {n:3d}x : {dist[n]:4d} tags")

    def report_duplicates(self, tags):
        self.h("NEAR-DUPLICATE GROUPS (spelling variants)")
        groups = defaultdict(list)
        for name, count in tags.items():
            groups[normalize(name)].append((name, count))

        found = 0
        for _, members in sorted(groups.items()):
            if len(members) > 1:
                found += 1
                members.sort(key=lambda x: -x[1])
                line = " | ".join(f"{n}({c})" for n, c in members)
                self.stdout.write(f"  {line}")
        if not found:
            self.stdout.write(self.style.SUCCESS("  none - vocabulary is clean"))
        else:
            self.stdout.write(f"\n  {found} groups. Semantic duplicates (ai vs "
                              "artificial-intelligence) are NOT caught here - "
                              "they need the eye, and a line in ALIASES.")

    def report_cut_line(self, posts, tags, threshold):
        self.h(f"CUT LINE SIMULATION (current threshold: {threshold})")
        self.stdout.write("  keeping only tags used >= N times:")
        for n in range(1, 6):
            keep = {t for t, c in tags.items() if c >= n}
            orphaned = sum(1 for t, _ in posts.values() if not (set(t) & keep))
            marker = "  <-- chosen" if n == threshold else ""
            self.stdout.write(
                f"    >={n}x : {len(keep):4d} tags kept, {orphaned:3d} posts left "
                f"with 0 tags{marker}"
            )

        below = sorted(t for t, c in tags.items() if c < threshold)
        self.stdout.write(f"\n  {len(below)} tags below the cut line:")
        self.stdout.write("  " + ", ".join(below))

    def report_untagged(self, posts):
        self.h("POSTS WITH NO TAGS")
        untagged = sorted(f for f, (t, _) in posts.items() if not t)
        self.stdout.write(f"  {len(untagged)} posts")
        for f in untagged:
            self.stdout.write(f"    {f}")

    def report_projects(self, tags):
        self.h("SHARED TAG TABLE: blog vs projects")
        project_tags = Counter()
        for project in Project.objects.all():
            for t in project.tags.values_list("name", flat=True):
                project_tags[t] += 1

        only_projects = sorted(set(project_tags) - set(tags))
        self.stdout.write("  used by Projects but never by a blog post:")
        for t in only_projects:
            self.stdout.write(f"    {project_tags[t]:4d}  {t}")

        shared = sorted(set(project_tags) & set(tags))
        self.stdout.write("\n  used by both (keep these spellings aligned):")
        for t in shared:
            self.stdout.write(f"    projects={project_tags[t]:<4d} posts={tags[t]:<4d} {t}")

        orphan_rows = Tag.objects.filter(publications=None, projects=None).count()
        if orphan_rows:
            self.stdout.write(
                f"\n  {orphan_rows} Tag rows in the DB attached to nothing "
                "(blogs-reindex garbage-collects these)."
            )

    def report_conformance(self, tags):
        self.h("VOCABULARY CONFORMANCE")
        unknown = sorted(
            t for t in tags
            if t not in VOCABULARY and t not in ALIASES and t not in DROP
        )
        if unknown:
            self.stdout.write(self.style.WARNING(
                f"  {len(unknown)} tags in use are not in VOCABULARY, ALIASES or DROP:"
            ))
            self.stdout.write("  " + ", ".join(unknown))
        else:
            self.stdout.write(self.style.SUCCESS(
                "  every tag in use is accounted for"
            ))

        applied_aliases = sorted(a for a in ALIASES if a not in tags)
        if applied_aliases:
            # Deliberately not listed in full: once applied these are just a
            # standing redirect table, and they should stay - they are what
            # catches an old spelling creeping back into a new post.
            self.stdout.write(
                f"\n  {len(applied_aliases)} of {len(ALIASES)} ALIASES no longer "
                "match any post - i.e. already applied. Keep them: they are the "
                "redirect table that stops the old spellings coming back."
            )

        unused = sorted(v for v in VOCABULARY if v not in tags)
        if unused:
            self.stdout.write(
                f"\n  {len(unused)} canonical tags in VOCABULARY unused by any post "
                "(fine if they are Project-only terms):"
            )
            self.stdout.write("  " + ", ".join(unused))

    def write_csv(self, path, tags, tag_to_posts):
        with open(path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["tag", "count", "facet", "canonical", "posts"])
            for name, count in tags.most_common():
                writer.writerow([
                    name,
                    count,
                    VOCABULARY.get(name, ""),
                    ALIASES.get(name, ""),
                    " ".join(tag_to_posts[name]),
                ])
        self.stdout.write("")
        self.stdout.write(self.style.SUCCESS(f"CSV written to {path}"))
