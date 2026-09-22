"""
The controlled category vocabulary for blog posts.

Categories are the blog's top-level sections - the coarse "which part of my
work is this" layer. Tags (see tag_vocabulary.py) do the fine-grained work, so
categories stay few and durable.

Decided 2026-09-22, replacing a set that had drifted into era markers:
  - `semantic-web` was a 2006-2014 career phase, dead since 2019
  - `informationarchitecture` was a 2000s web-design term, and 13 of its 41
    posts were also `semantic-web` - the largest overlap in the old set
  - both merge into `knowledge-engineering`, which is era-neutral
  - `research-analytics` is new: ~25 posts spanning 2014-2026 that were
    scattered across SIX categories with no home of their own
  - `digitalhumanities` -> `digital-humanities`, name only. Kept deliberately:
    it is dormant professionally but it is what the 2026 posts are about.

BOUNDARY RULE, to stop the old overlap problem coming back:
    research-analytics   = the DOMAIN. The post is about scholarly/research
                           data - publications, citations, funders, metrics -
                           whatever technology it uses. SciGraph posts live
                           here, not in knowledge-engineering.
    knowledge-engineering = the METHOD. Ontologies, RDF, modelling,
                           taxonomies, faceted search.
    data-science         = working with data: notebooks, dashboards, charts.

Used by:
    manage.py categories_apply    rewrites the markdown frontmatter to match

Markdown is the source of truth (see TAGS_PLAN.md); the DB is a derived index.
"""

# The only categories allowed. Anything else is an error.
CATEGORIES = {
    "computermusic": "Livecoding, algorithmic composition, music made with code",
    "knowledge-engineering": "Ontologies, RDF, modelling, taxonomies, faceted search",
    "research-analytics": "Scholarly data: publications, citations, funders, metrics",
    "digital-humanities": "Reading texts as data; philosophy, classics, cultural heritage",
    "data-science": "Working with data: notebooks, dashboards, visualisation",
    "techlife": "Tools and craft: the software I use and build",
    "justblogging": "Everything else",
}

# Renames applied to every post that carries the old name.
RENAMES = {
    "digitalhumanities": "digital-humanities",
    "semantic-web": "knowledge-engineering",
    "informationarchitecture": "knowledge-engineering",
}

# Explicit per-post result, for every post whose categories change. Generated
# from the rules above plus hand routing of the posts that needed a decision,
# then frozen here so the mapping is reviewable rather than hidden in logic.
# `md_file` is the post id (see do_blogs_reindex).

POST_CATEGORIES = {
    "2006-06-29-compendium-vs-nestor.md":
        ['knowledge-engineering'],   # was ['informationarchitecture']
    "2006-06-29-review-automatist-storyteller-systems-and-the-shifting-sands-of-story-by-g-davenport-and-m-murtaugh.md":
        ['digital-humanities', 'justblogging'],   # was ['digitalhumanities', 'justblogging']
    "2006-07-19-a-random-walk-through-the-20th-century.md":
        ['digital-humanities'],   # was ['digitalhumanities']
    "2006-10-04-navigating-the-rijksmuseum.md":
        ['digital-humanities'],   # was ['digitalhumanities']
    "2006-10-23-semantic-wikipedia-some-issues.md":
        ['knowledge-engineering'],   # was ['semantic-web']
    "2006-10-24-lets-visualize-em.md":
        ['digital-humanities', 'techlife'],   # was ['digitalhumanities', 'techlife']
    "2006-11-21-web-30.md":
        ['knowledge-engineering'],   # was ['semantic-web']
    "2006-11-23-multimedian-semantic-navigator.md":
        ['digital-humanities', 'knowledge-engineering'],   # was ['digitalhumanities', 'semantic-web']
    "2006-11-28-pathway-wiki-semantic-navigator.md":
        ['knowledge-engineering'],   # was ['semantic-web']
    "2006-11-28-the-nora-project.md":
        ['digital-humanities'],   # was ['digitalhumanities']
    "2006-11-30-knowledge-elicitation-playing-with-cards.md":
        ['knowledge-engineering'],   # was ['informationarchitecture']
    "2007-01-05-text-encoding-initiative-a-historical-paper.md":
        ['digital-humanities', 'justblogging', 'knowledge-engineering'],   # was ['digitalhumanities', 'justblogging', 'semantic-web']
    "2007-01-18-the-internet-classics-archive.md":
        ['digital-humanities'],   # was ['digitalhumanities']
    "2007-01-26-turning-the-pages-of-literature.md":
        ['digital-humanities'],   # was ['digitalhumanities']
    "2007-02-01-philosophical-search-engine.md":
        ['digital-humanities'],   # was ['digitalhumanities']
    "2007-02-06-lisp-conference-in-cambridge.md":
        ['knowledge-engineering'],   # was ['semantic-web']
    "2007-02-21-nines-sw-faceted-browser-by-speclab.md":
        ['digital-humanities', 'knowledge-engineering', 'techlife'],   # was ['digitalhumanities', 'semantic-web', 'techlife']
    "2007-03-05-ontology-of-representations.md":
        ['knowledge-engineering'],   # was ['informationarchitecture']
    "2007-03-30-modeling-representations-take-2.md":
        ['knowledge-engineering'],   # was ['informationarchitecture']
    "2007-04-02-indiana-philosophy-ontology-project.md":
        ['digital-humanities', 'knowledge-engineering'],   # was ['digitalhumanities', 'informationarchitecture']
    "2007-04-19-carnap-on-syntax.md":
        ['justblogging', 'knowledge-engineering'],   # was ['justblogging', 'semantic-web']
    "2007-06-04-philosophy-on-the-air.md":
        ['digital-humanities', 'justblogging'],   # was ['digitalhumanities', 'justblogging']
    "2007-06-07-sw-vs-ai-new-and-old-stuff.md":
        ['knowledge-engineering'],   # was ['justblogging', 'semantic-web']
    "2007-06-12-discovery-philosophy-in-the-digital-era.md":
        ['digital-humanities', 'knowledge-engineering'],   # was ['digitalhumanities', 'semantic-web']
    "2007-06-25-what-can-the-analytical-engine-do-ask-charles-babbage.md":
        ['justblogging', 'knowledge-engineering'],   # was ['justblogging', 'semantic-web']
    "2007-06-27-30th-international-wittgenstein-symposium.md":
        ['digital-humanities', 'justblogging'],   # was ['digitalhumanities', 'justblogging']
    "2007-09-03-wheres-all-the-time-gone.md":
        ['digital-humanities'],   # was ['justblogging']
    "2007-09-12-dbpedia-rocks.md":
        ['knowledge-engineering'],   # was ['semantic-web']
    "2007-09-24-zotero-is-the-browser-enough-to-do-research.md":
        ['digital-humanities', 'justblogging'],   # was ['digitalhumanities', 'justblogging']
    "2008-01-13-how-semantic-is-the-semantic-web.md":
        ['knowledge-engineering'],   # was ['justblogging', 'semantic-web']
    "2008-02-04-humanities-computing-and-web2.md":
        ['digital-humanities', 'justblogging'],   # was ['digitalhumanities', 'justblogging']
    "2008-02-12-epistemic-logic.md":
        ['knowledge-engineering'],   # was ['semantic-web']
    "2008-02-26-new-philosurfical-version.md":
        ['digital-humanities'],   # was ['justblogging']
    "2008-03-06-new-book-on-knowledge-technologies.md":
        ['knowledge-engineering'],   # was ['semantic-web']
    "2008-03-10-the-british-wittgenstein-society-gets-started.md":
        ['digital-humanities'],   # was ['justblogging']
    "2009-01-07-musicbox-maps-future-for-managing-large-music-collections.md":
        ['digital-humanities'],   # was ['digitalhumanities']
    "2009-03-02-gae-sql-designer.md":
        ['knowledge-engineering', 'techlife'],   # was ['informationarchitecture', 'techlife']
    "2009-03-05-faceted-browsing-a-conceptual-map.md":
        ['knowledge-engineering'],   # was ['informationarchitecture']
    "2009-03-10-db-visualize-the-universal-database-tool.md":
        ['knowledge-engineering', 'techlife'],   # was ['informationarchitecture', 'techlife']
    "2009-05-02-a-sneak-preview-of-wolframalpha.md":
        ['knowledge-engineering', 'techlife'],   # was ['semantic-web', 'techlife']
    "2009-05-14-layer-the-web-with-blerp.md":
        ['digital-humanities', 'knowledge-engineering', 'techlife'],   # was ['digitalhumanities', 'semantic-web', 'techlife']
    "2009-06-03-wordsift-visualize-text.md":
        ['digital-humanities', 'techlife'],   # was ['digitalhumanities', 'techlife']
    "2009-06-18-understanding-googles-bigtable.md":
        ['knowledge-engineering', 'techlife'],   # was ['informationarchitecture', 'techlife']
    "2009-06-19-logic-and-ontology.md":
        ['knowledge-engineering'],   # was ['informationarchitecture', 'semantic-web']
    "2009-07-21-roman-port-networks-project.md":
        ['digital-humanities'],   # was ['digitalhumanities']
    "2009-07-31-nlp-for-classical-studies.md":
        ['digital-humanities'],   # was ['digitalhumanities']
    "2009-08-06-representing-hierarchical-data-with-django-and-mptt.md":
        ['knowledge-engineering', 'techlife'],   # was ['informationarchitecture', 'techlife']
    "2009-08-21-social-reference-manager-mendeley.md":
        ['digital-humanities', 'techlife'],   # was ['digitalhumanities', 'techlife']
    "2009-10-20-uml-to-django.md":
        ['knowledge-engineering'],   # was ['informationarchitecture']
    "2009-10-31-wittgensteins-tractatus.md":
        ['digital-humanities'],   # was ['digitalhumanities']
    "2010-02-04-getting-back-to-the-ontological-work.md":
        ['knowledge-engineering'],   # was ['semantic-web']
    "2010-07-26-knowledge-representation-workshop-cch.md":
        ['knowledge-engineering'],   # was ['informationarchitecture', 'semantic-web']
    "2010-08-30-kr-workshop-2-introducing-cidoc-crm-and-frbr-oo.md":
        ['digital-humanities', 'knowledge-engineering'],   # was ['digitalhumanities', 'informationarchitecture', 'semantic-web']
    "2010-09-16-musorg-tons-of-classical-music-for-free.md":
        ['computermusic'],   # was ['justblogging']
    "2010-09-19-nodictionaries-com-innovative-way-to-read-latin-classics.md":
        ['digital-humanities'],   # was ['digitalhumanities']
    "2010-10-14-amazons-kindle-is-slowly-changing-my-life.md":
        ['digital-humanities', 'justblogging'],   # was ['digitalhumanities', 'justblogging']
    "2010-12-09-livecoding-xmas-event-at-goldsmith-college.md":
        ['computermusic'],   # was ['justblogging']
    "2011-02-24-survey-of-pythonic-tools-for-rdf-and-linked-data-programming.md":
        ['knowledge-engineering', 'techlife'],   # was ['semantic-web', 'techlife']
    "2011-03-17-a-few-useful-linked-data-resources.md":
        ['knowledge-engineering'],   # was ['semantic-web']
    "2011-04-14-allegro-cl-graph.md":
        ['knowledge-engineering', 'techlife'],   # was ['semantic-web', 'techlife']
    "2011-05-23-hack4europe-europeana-hackathon-roadshow-june-2011.md":
        ['digital-humanities', 'knowledge-engineering'],   # was ['digitalhumanities', 'semantic-web']
    "2011-06-09-djfacet-a-django-faceted-browser.md":
        ['knowledge-engineering', 'techlife'],   # was ['informationarchitecture', 'techlife']
    "2011-06-30-digital-humanities-conference-2011-a-short-review.md":
        ['digital-humanities'],   # was ['digitalhumanities']
    "2011-07-11-workshop-on-live-coding-rmll-11.md":
        ['computermusic'],   # was ['justblogging']
    "2011-07-18-inspecting-an-ontology-with-rdflib.md":
        ['knowledge-engineering', 'techlife'],   # was ['semantic-web', 'techlife']
    "2011-09-28-event-thatcamp-kansas-and-digital-humanities-forum.md":
        ['digital-humanities'],   # was ['digitalhumanities']
    "2011-09-29-luc-steels-on-creating-artificial-semiotic-systems.md":
        ['knowledge-engineering'],   # was ['justblogging']
    "2011-10-13-seminar-tagore-digital-editions-and-bengali-textual-computing.md":
        ['digital-humanities'],   # was ['digitalhumanities']
    "2011-11-19-towards-a-conceptual-model-for-the-domain-of-sculpture.md":
        ['digital-humanities', 'knowledge-engineering'],   # was ['digitalhumanities', 'informationarchitecture']
    "2012-03-01-the-future-of-the-book.md":
        ['digital-humanities', 'techlife'],   # was ['digitalhumanities', 'techlife']
    "2012-03-28-conference-computer-applications-and-quantitative-methods-in-archeology.md":
        ['digital-humanities'],   # was ['digitalhumanities']
    "2012-05-16-djfacet-0-9-7-mptt-hierarchical-facets-now-supported.md":
        ['knowledge-engineering'],   # was ['informationarchitecture']
    "2012-05-24-the-role-of-digital-humanities-in-a-natural-disaster.md":
        ['digital-humanities'],   # was ['digitalhumanities']
    "2012-06-01-crowdsourcing-interpretation-with-prism-a-new-software-from-the-scholars-lab.md":
        ['digital-humanities'],   # was ['digitalhumanities']
    "2012-07-08-wittgenstein-and-the-javascript-infovis-toolkit.md":
        ['digital-humanities'],   # was ['digitalhumanities']
    "2012-09-10-navigating-through-the-people-of-medieval-scotland.md":
        ['digital-humanities', 'knowledge-engineering'],   # was ['digitalhumanities', 'informationarchitecture']
    "2012-09-21-open-knowledge-festival-helsinki-18-22-september-2012.md":
        ['knowledge-engineering'],   # was ['justblogging']
    "2012-11-06-infographics-course-week-1.md":
        ['data-science'],   # was ['informationarchitecture']
    "2012-11-14-infographics-course-week-2.md":
        ['data-science'],   # was ['informationarchitecture']
    "2012-11-27-semantic-web-cheat-sheets.md":
        ['knowledge-engineering'],   # was ['semantic-web']
    "2013-04-10-an-introduction-to-neo4j.md":
        ['knowledge-engineering'],   # was ['informationarchitecture']
    "2013-04-27-annual-bliss-classification-association-lecture-using-faceted-browsers-in-the-dh.md":
        ['digital-humanities', 'justblogging'],   # was ['digitalhumanities', 'justblogging']
    "2013-05-20-rdf-semantics-genius-or-madness.md":
        ['knowledge-engineering'],   # was ['informationarchitecture', 'semantic-web']
    "2013-06-05-eswc-2013-report-from-the-conference.md":
        ['knowledge-engineering'],   # was ['justblogging', 'semantic-web']
    "2013-06-21-messing-around-wih-d3-js-and-hierarchical-data.md":
        ['data-science'],   # was ['informationarchitecture']
    "2013-07-25-creating-useful-classifications-with-taxonomies-part-1.md":
        ['knowledge-engineering'],   # was ['informationarchitecture']
    "2013-08-13-textmate-bundle-for-turtle-and-sparql.md":
        ['knowledge-engineering', 'techlife'],   # was ['semantic-web', 'techlife']
    "2013-12-16-annotating-the-web-with-scrible.md":
        ['digital-humanities', 'justblogging'],   # was ['digitalhumanities', 'justblogging']
    "2014-06-23-nature-com-subject-pages-available-online.md":
        ['research-analytics'],   # was ['informationarchitecture', 'justblogging', 'semantic-web']
    "2014-08-22-visualising-a-big-taxonomy-in-a-small-screen-in-pure-html.md":
        ['data-science'],   # was ['informationarchitecture']
    "2014-10-12-interactive-turtle-shell.md":
        ['knowledge-engineering'],   # was ['informationarchitecture', 'semantic-web']
    "2014-10-16-getting-started-with-a-triplestore-on-mac-os-graphdb-aka-owlim.md":
        ['knowledge-engineering', 'techlife'],   # was ['semantic-web', 'techlife']
    "2014-10-27-getting-started-with-a-triplestore-on-mac-os-cliopatria.md":
        ['knowledge-engineering', 'techlife'],   # was ['semantic-web', 'techlife']
    "2014-11-06-installing-stardog-triplestore-on-mac-os.md":
        ['knowledge-engineering', 'techlife'],   # was ['semantic-web', 'techlife']
    "2014-11-25-iswc14-paper-a-hybrid-semantic-publishing-architecture-combining-xml-and-rdf.md":
        ['research-analytics'],   # was ['justblogging', 'semantic-web']
    "2014-12-22-italian-public-spending-data.md":
        ['data-science'],   # was ['informationarchitecture', 'semantic-web']
    "2015-01-05-introducing-resquotes-com.md":
        ['digital-humanities', 'justblogging'],   # was ['digitalhumanities', 'justblogging']
    "2015-01-17-notes-from-the-force11-annual-conference.md":
        ['research-analytics'],   # was ['justblogging']
    "2015-04-30-nature-com-ontologies-portal-available-online.md":
        ['research-analytics'],   # was ['justblogging', 'semantic-web']
    "2015-06-08-a-sneak-peek-at-nature-com-articles-archive.md":
        ['data-science', 'research-analytics'],   # was ['justblogging', 'semantic-web']
    "2015-06-14-recent-projects-from-crossref-org.md":
        ['research-analytics'],   # was ['justblogging', 'semantic-web']
    "2015-06-17-towards-an-ontology-for-philosophy-really.md":
        ['digital-humanities', 'knowledge-engineering'],   # was ['digitalhumanities', 'semantic-web']
    "2015-09-02-is-wikipedia-a-valid-source-of-scientific-knowledge.md":
        ['research-analytics'],   # was ['informationarchitecture', 'semantic-web']
    "2015-09-21-another-experiment-with-wittgensteins-tractatus.md":
        ['digital-humanities', 'knowledge-engineering'],   # was ['digitalhumanities', 'informationarchitecture']
    "2016-01-03-nature-com-subjects-stream-graph.md":
        ['research-analytics'],   # was ['informationarchitecture']
    "2016-06-12-ontospy-v-1-6-7.md":
        ['knowledge-engineering'],   # was ['informationarchitecture', 'semantic-web']
    "2016-10-21-open-data-summit-2016.md":
        ['research-analytics'],   # was ['justblogging', 'semantic-web']
    "2016-10-25-leipzig-semantics-2016-conference.md":
        ['research-analytics'],   # was ['justblogging', 'semantic-web']
    "2017-02-27-ontospy-v-1-7-4.md":
        ['knowledge-engineering', 'techlife'],   # was ['semantic-web', 'techlife']
    "2017-04-06-exploring-scigraph-data-using-elastic-search-and-kibana.md":
        ['research-analytics'],   # was ['informationarchitecture', 'semantic-web']
    "2017-11-14-scigraph-publishes-1-billion-facts-as-linked-open-data.md":
        ['research-analytics'],   # was ['semantic-web']
    "2018-03-22-interesting-read-scisci-i-e-the-science-of-science.md":
        ['digital-humanities', 'research-analytics'],   # was ['digitalhumanities', 'justblogging']
    "2018-05-23-sn-scigraph-is-part-of-the-linked-open-data-cloud-2018.md":
        ['research-analytics'],   # was ['semantic-web']
    "2018-06-07-pyscigraph-simple-api-for-accessing-springer-nature-scigraph-content.md":
        ['research-analytics'],   # was ['semantic-web']
    "2018-08-01-sn-scigraph-latest-website-release-make-it-easier-to-discover-related-content.md":
        ['research-analytics'],   # was ['informationarchitecture', 'semantic-web']
    "2018-11-23-exploring-scholarly-publications-via-dbpedia.md":
        ['research-analytics'],   # was ['informationarchitecture', 'semantic-web']
    "2019-01-03-ontospy-1-9-8-released.md":
        ['knowledge-engineering'],   # was ['informationarchitecture', 'semantic-web']
    "2019-02-11-zero-hunger-hack-day.md":
        ['research-analytics'],   # was ['informationarchitecture', 'justblogging']
    "2019-03-22-sn-scigraph-latest-release-patents-clinical-trials-and-many-new-features.md":
        ['research-analytics'],   # was ['semantic-web']
    "2019-05-24-introducing-dimcli-a-python-cli-for-dimensions-api.md":
        ['data-science', 'research-analytics', 'techlife'],   # was ['data-science', 'techlife']
    "2019-06-30-pypapers-a-bare-bones-command-line-pdf-manager.md":
        ['digital-humanities', 'techlife'],   # was ['digitalhumanities', 'techlife']
    "2020-01-08-calculating-industry-collaborations-via-grid.md":
        ['data-science', 'research-analytics'],   # was ['data-science']
    "2021-01-22-the-kryos-noise-is-available-on-spotify.md":
        ['computermusic'],   # was ['justblogging']
    "2021-04-02-Hydra.md":
        ['computermusic'],   # was ['justblogging']
    "2022-03-02-Three-things-i-like-about-looker.md":
        ['data-science'],   # was ['informationarchitecture']
    "2022-04-20-Three-things-i-do-not-like-about-looker.md":
        ['data-science'],   # was ['informationarchitecture']
    "2022-06-30-a-semi-automated-conference-assistant.md":
        ['research-analytics', 'techlife'],   # was ['techlife']
    "2022-07-28-introducing-quotes-section.md":
        ['data-science'],   # was ['informationarchitecture']
    "2023-02-03-rip-scigraph.md":
        ['research-analytics'],   # was ['justblogging']
    "2023-07-06-designing-great-dashboards.md":
        ['data-science'],   # was ['informationarchitecture']
    "2024-09-27-open-alex-topics.md":
        ['data-science', 'research-analytics'],   # was ['data-science']
    "2026-03-03-shifting-landscape-research-analytics.md":
        ['research-analytics'],   # was ['justblogging']
    "2026-04-21-funding-flows-global-south-clacso.md":
        ['research-analytics'],   # was ['justblogging']
    "2026-08-17-five-new-ways-to-read-the-tractatus.md":
        ['digital-humanities'],   # was ['digitalhumanities']
    "2026-09-02-reading-naples-44-as-a-database.md":
        ['digital-humanities'],   # was ['digitalhumanities']
}
