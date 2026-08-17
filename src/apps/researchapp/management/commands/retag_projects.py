"""
One-off data migration: replace the Project tag set with a cleaned-up,
faceted vocabulary (domain / format / tech) instead of the old flat mix
of hack / prototype / data / science / nlp / ontology etc.

Tag is shared between Project and Publication (see Tag model docstring),
so this command only changes which Tag rows are attached to Projects -
it never renames or deletes a Tag, and reuses Tag rows Publications
already use (semanticweb, livecoding, python, lisp) rather than creating
near-duplicates.

Usage:
    python manage.py retag_projects            # dry run, prints diff
    python manage.py retag_projects --apply     # actually writes changes
"""

from django.core.management.base import BaseCommand
from researchapp.models import Project, Tag


# urlstub -> list of new tag names (domain + format + tech)
# Outliers (zavreldreams, pypapers, liquidquotes) intentionally have no
# domain tag, per 2026-08-17 decision.
NEW_TAGS = {
    "wittgensteiniana": ["digital-humanities", "visualization"],
    "zavreldreams": ["website"],
    "pubreports": ["research-analytics", "dashboard"],
    "dimensionscovid": ["research-analytics", "dashboard"],
    "dimensionsapilabs": ["research-analytics", "tool", "python"],
    "dimcli": ["research-analytics", "tool", "python"],
    "scigraph": ["research-analytics", "semanticweb", "website"],
    "pypapers": ["tool", "python"],
    "dbpedia2scigraph": ["research-analytics", "visualization"],
    "zerohunger2018": ["research-analytics", "visualization"],
    "sganalytics": ["research-analytics", "dashboard"],
    "ontodocs": ["semanticweb", "tool", "python"],
    "npgstreamgraph": ["research-analytics", "visualization"],
    "ontospy": ["semanticweb", "tool", "python"],
    "npgwikipedia": ["research-analytics", "visualization"],
    "natureontologyportal": ["semanticweb", "website"],
    "impromptudocs": ["livecoding", "tool"],
    "liquidquotes": ["tool"],
    "npgsubjectstree": ["research-analytics", "semanticweb", "visualization"],
    "npgsubjectpages": ["research-analytics", "website"],
    "artofmaking": ["digital-humanities", "website"],
    "pomslabs": ["digital-humanities", "visualization"],
    "poms": ["digital-humanities", "website"],
    "bob": ["digital-humanities", "website"],
    "mkcheur": ["digital-humanities", "website"],
    "sails": ["digital-humanities", "semanticweb", "tool"],
    "emlot": ["digital-humanities", "website"],
    "philosurfical": ["digital-humanities", "semanticweb", "website"],
    "cohere": ["semanticweb", "tool"],
    "irs": ["semanticweb", "tool"],
    "aqualog": ["semanticweb", "tool"],
    "hucit": ["digital-humanities", "semanticweb", "tool"],
    "dimensionsgbqlab": ["research-analytics", "tool"],
    "dimensionsmenubar": ["research-analytics", "tool", "python"],
    "dimensionsbigquery": ["research-analytics", "tool"],
    "xtm-extensions": ["livecoding", "tool", "lisp"],
    "dim-network-gen": ["research-analytics", "visualization", "python"],
    "dimensions_p_and_i": ["research-analytics", "dashboard"],
    "dimensions_l_and_d": ["research-analytics", "dashboard"],
    "themusicalcode": ["livecoding", "tool", "lisp"],
    "dimensions_recsec": ["research-analytics", "dashboard"],
    "oalex_topics": ["research-analytics", "visualization"],
}


class Command(BaseCommand):
    help = "Retag Project records with the new domain/format/tech facet vocabulary. Dry-run by default."

    def add_arguments(self, parser):
        parser.add_argument(
            "--apply",
            action="store_true",
            help="Actually write the changes. Without this flag, only a diff is printed.",
        )

    def handle(self, *args, **options):
        apply_changes = options["apply"]

        projects = {p.urlstub: p for p in Project.objects.all()}

        missing = set(projects) - set(NEW_TAGS)
        unknown = set(NEW_TAGS) - set(projects)
        if missing:
            self.stderr.write(self.style.WARNING(
                f"No mapping defined for these existing projects (left untouched): {sorted(missing)}"
            ))
        if unknown:
            self.stderr.write(self.style.WARNING(
                f"Mapping references urlstubs that don't exist in the DB: {sorted(unknown)}"
            ))

        for urlstub, tag_names in NEW_TAGS.items():
            project = projects.get(urlstub)
            if not project:
                continue

            old_names = sorted(project.tags.values_list("name", flat=True))
            new_names = sorted(tag_names)

            if old_names == new_names:
                continue

            self.stdout.write(f"{project.title} ({urlstub})")
            self.stdout.write(f"  - old: {old_names}")
            self.stdout.write(f"  + new: {new_names}")

            if apply_changes:
                tag_objs = []
                for name in tag_names:
                    tag, _ = Tag.objects.get_or_create(name=name)
                    tag_objs.append(tag)
                project.tags.set(tag_objs)

        if apply_changes:
            self.stdout.write(self.style.SUCCESS("Applied."))
        else:
            self.stdout.write(self.style.WARNING("Dry run only - re-run with --apply to write changes."))
