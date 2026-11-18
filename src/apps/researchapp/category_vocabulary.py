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
    knowledge-engineering also takes AI and LLMs (since 2026-11-18).

Revised 2026-11-18 (backlog #7, plan in backlog/plans/007-category-cleanup.md):
seven categories, five topics and two kinds, after a review of every post.
  - `justblogging` is retired. Its posts went to a topic where one fits, else
    to `techlife` or the new `reviews`.
  - Slugs are kept for the renamed topics, so ?ctype= links don't break; the
    new names live in CATEGORY_LABELS (templatetags/extrafilters.py):
    knowledge-engineering = AI & Knowledge Graphs, data-science = Data &
    Visualisation, computermusic = Music & Art, techlife = Tech & Tools.

PRECEDENCE RULE: a topic first. A post goes into one of the five topics if it
is genuinely about that work, whatever its format (an opinion piece on AI is
knowledge-engineering only). `techlife` and `reviews` are only for posts that
no topic fits.

Used by:
    manage.py categories_apply    rewrites the markdown frontmatter to match

Markdown is the source of truth (see TAGS_PLAN.md); the DB is a derived index.
"""

# The only categories allowed. Anything else is an error.
CATEGORIES = {
    # topics: what the post is about
    "knowledge-engineering": "AI and knowledge graphs: ontologies, RDF, modelling, LLMs",
    "research-analytics": "Scholarly data: publications, citations, funders, metrics",
    "data-science": "Working with data: notebooks, dashboards, visualisation",
    "digital-humanities": "Reading texts as data; philosophy, classics, cultural heritage",
    "computermusic": "Music and art: livecoding, music I listen to, visual and interactive art",
    # kinds: only for posts no topic fits
    "techlife": "Tech and tools: how-tos, tips, software I use and build",
    "reviews": "Reviews and opinions: books, tools, sites, essays, events",
}

# Renames applied to every post that carries the old name. `justblogging` has
# no rename on purpose: it split three ways, so a post still carrying it must
# get a line in POST_CATEGORIES (categories_apply refuses otherwise).
RENAMES = {
    "digitalhumanities": "digital-humanities",
    "semantic-web": "knowledge-engineering",
    "informationarchitecture": "knowledge-engineering",
}

# Explicit per-post result, for every post whose categories change. Frozen from
# the 2026-11-18 review (backlog/plans/007-category-cleanup/review-decisions-2026-11-18.json)
# so the mapping is reviewable rather than hidden in logic. The 2026-09-22
# entries this replaces are in git history. `md_file` is the post id (see
# do_blogs_reindex).

POST_CATEGORIES = {
    "2006-03-06-a-doctor-hidden-in-the-mac.md":
        ['knowledge-engineering'],   # was ['justblogging']
    "2006-04-06-library-20.md":
        ['digital-humanities'],   # was ['justblogging']
    "2006-06-29-review-automatist-storyteller-systems-and-the-shifting-sands-of-story-by-g-davenport-and-m-murtaugh.md":
        ['digital-humanities'],   # was ['digital-humanities', 'justblogging']
    "2006-10-09-howar-gardners-talk.md":
        ['reviews'],   # was ['justblogging']
    "2006-10-24-lets-visualize-em.md":
        ['data-science'],   # was ['digital-humanities', 'techlife']
    "2006-10-28-firefox-20-will-i-ever-go-back-to-safari.md":
        ['reviews'],   # was ['justblogging']  # not in the review (in review or newer); placed by hand
    "2006-10-29-132.md":
        ['reviews'],   # was ['justblogging']
    "2006-11-02-free-learning-resources-from-the-ou.md":
        ['reviews'],   # was ['justblogging']
    "2006-12-01-a-cyberspace-atlas.md":
        ['data-science'],   # was ['justblogging']
    "2006-12-04-smultron-text-editor.md":
        ['techlife'],   # was ['justblogging']
    "2006-12-12-fink-fhink-think.md":
        ['reviews'],   # was ['justblogging']
    "2006-12-19-end-of-ou-broadcasting.md":
        ['reviews'],   # was ['justblogging']
    "2007-01-05-text-encoding-initiative-a-historical-paper.md":
        ['digital-humanities', 'knowledge-engineering'],   # was ['digital-humanities', 'justblogging', 'knowledge-engineering']
    "2007-01-10-visiting-the-digilab.md":
        ['digital-humanities'],   # was ['justblogging']
    "2007-01-11-ichat-to-msn-only-one-im-client-please.md":
        ['techlife'],   # was ['justblogging']
    "2007-01-17-macfuse-gmail-gigs-on-the-desktop.md":
        ['reviews'],   # was ['justblogging']
    "2007-01-17-where-is-italy.md":
        ['reviews'],   # was ['justblogging']  # not in the review (in review or newer); placed by hand
    "2007-01-22-hand-controlled-wah.md":
        ['computermusic'],   # was ['justblogging']
    "2007-01-24-google-map-goes-down-to-the-humans.md":
        ['reviews'],   # was ['justblogging']
    "2007-02-06-lisp-conference-in-cambridge.md":
        ['reviews'],   # was ['knowledge-engineering']
    "2007-02-21-nines-sw-faceted-browser-by-speclab.md":
        ['digital-humanities', 'knowledge-engineering'],   # was ['digital-humanities', 'knowledge-engineering', 'techlife']
    "2007-03-02-dear-old-paper-how-could-we-do-without-you.md":
        ['reviews'],   # was ['justblogging']
    "2007-03-14-internet-research-ethics-a-first-journal.md":
        ['digital-humanities'],   # was ['justblogging']
    "2007-03-15-ecto-multiple-blog-manager-and-wusiwyg-editor.md":
        ['techlife'],   # was ['justblogging']
    "2007-03-19-navigating-the-eternal-egypt.md":
        ['digital-humanities'],   # was ['justblogging']
    "2007-03-21-lyx-on-the-mac.md":
        ['techlife'],   # was ['justblogging']
    "2007-03-22-digital-document-quarterly.md":
        ['digital-humanities'],   # was ['justblogging']
    "2007-04-17-hypernietzsche.md":
        ['digital-humanities'],   # was ['justblogging']
    "2007-04-19-carnap-on-syntax.md":
        ['knowledge-engineering'],   # was ['justblogging', 'knowledge-engineering']
    "2007-04-24-what-lisp-to-choose-really.md":
        ['techlife'],   # was ['justblogging']
    "2007-05-11-new-macs-too-new-for-me.md":
        ['techlife'],   # was ['justblogging']
    "2007-05-18-lispdoc-online-lisp-documentation-search.md":
        ['reviews'],   # was ['techlife']
    "2007-05-31-go-get-the-milk.md":
        ['computermusic'],   # was ['justblogging']
    "2007-06-04-philosophy-on-the-air.md":
        ['digital-humanities'],   # was ['digital-humanities', 'justblogging']
    "2007-06-09-aquamacs-10.md":
        ['reviews'],   # was ['techlife']
    "2007-06-20-conference-saso-2007.md":
        ['reviews'],   # was ['justblogging']
    "2007-06-25-what-can-the-analytical-engine-do-ask-charles-babbage.md":
        ['knowledge-engineering'],   # was ['justblogging', 'knowledge-engineering']
    "2007-06-27-30th-international-wittgenstein-symposium.md":
        ['digital-humanities', 'reviews'],   # was ['digital-humanities', 'justblogging']
    "2007-09-03-wheres-all-the-time-gone.md":
        ['reviews'],   # was ['digital-humanities']
    "2007-09-07-vaffanculo-day.md":
        ['reviews'],   # was ['justblogging']  # not in the review (in review or newer); placed by hand
    "2007-09-24-zotero-is-the-browser-enough-to-do-research.md":
        ['digital-humanities', 'reviews'],   # was ['digital-humanities', 'justblogging']
    "2007-09-28-jamendo-free-and-quality-music-online.md":
        ['computermusic'],   # was ['justblogging']
    "2007-10-11-mmm-that-ruby-is-hot.md":
        ['techlife'],   # was ['justblogging']
    "2007-11-06-love-trippin.md":
        ['reviews'],   # was ['techlife']
    "2008-02-04-humanities-computing-and-web2.md":
        ['digital-humanities', 'reviews'],   # was ['digital-humanities', 'justblogging']
    "2008-03-07-social-innovation-camp-in-london.md":
        ['reviews'],   # was ['justblogging']
    "2008-03-10-the-british-wittgenstein-society-gets-started.md":
        ['digital-humanities', 'reviews'],   # was ['digital-humanities']
    "2008-04-03-comparing-programming-languages.md":
        ['techlife'],   # was ['justblogging']
    "2008-07-10-quotation-from-gregory-bateson.md":
        ['reviews'],   # was ['justblogging']
    "2009-01-06-pythons-phenotype.md":
        ['reviews'],   # was ['justblogging', 'techlife']
    "2009-01-07-musicbox-maps-future-for-managing-large-music-collections.md":
        ['computermusic', 'data-science'],   # was ['digital-humanities']
    "2009-01-26-apple-introduces-revolutionary-new-laptop-with-no-keyboard.md":
        ['reviews'],   # was ['justblogging']
    "2009-01-27-how-to-make-a-mac-screen-saver-that-shows-your-uptime.md":
        ['techlife'],   # was ['justblogging']
    "2009-01-31-google-flags-whole-internet-as-malware.md":
        ['reviews'],   # was ['justblogging']
    "2009-03-02-gae-sql-designer.md":
        ['techlife'],   # was ['knowledge-engineering', 'techlife']
    "2009-03-05-faceted-browsing-a-conceptual-map.md":
        ['data-science', 'digital-humanities'],   # was ['knowledge-engineering']
    "2009-03-10-db-visualize-the-universal-database-tool.md":
        ['techlife'],   # was ['knowledge-engineering', 'techlife']
    "2009-03-25-academic-earth-hours-of-free-lectures-online.md":
        ['reviews'],   # was ['justblogging']
    "2009-04-02-augmented-reality-with-mits-sixth-sense-game-changing-wearable-tech.md":
        ['reviews'],   # was ['computermusic']
    "2009-04-28-spread-the-word-the-italian-circus-goes-to-the-eu.md":
        ['reviews'],   # was ['justblogging']
    "2009-05-02-a-sneak-preview-of-wolframalpha.md":
        ['knowledge-engineering'],   # was ['knowledge-engineering', 'techlife']
    "2009-05-04-freedom-of-press-is-that-asking-too-much.md":
        ['reviews'],   # was ['justblogging']
    "2009-05-07-installing-rdflib-on-osx.md":
        ['knowledge-engineering', 'techlife'],   # was ['techlife']
    "2009-05-07-soundmanager-2-makes-it-easier-to-play-sounds-using-javascript.md":
        ['computermusic'],   # was ['techlife']
    "2009-05-14-layer-the-web-with-blerp.md":
        ['digital-humanities'],   # was ['digital-humanities', 'knowledge-engineering', 'techlife']
    "2009-05-20-how-to-get-the-iphone-to-stop-automatic-back-ups.md":
        ['techlife'],   # was ['justblogging', 'techlife']
    "2009-06-03-wordsift-visualize-text.md":
        ['digital-humanities'],   # was ['digital-humanities', 'techlife']
    "2009-06-09-visualizing-bach-toccata-and-fugue-in-d-minor-organ.md":
        ['computermusic', 'data-science'],   # was ['computermusic']
    "2009-06-18-understanding-googles-bigtable.md":
        ['techlife'],   # was ['knowledge-engineering', 'techlife']
    "2009-08-01-end-of-this-adventure.md":
        ['reviews'],   # was ['justblogging']
    "2009-08-06-representing-hierarchical-data-with-django-and-mptt.md":
        ['data-science'],   # was ['knowledge-engineering', 'techlife']
    "2009-08-21-satire-you-wont-be-able-to-listen-to-in-italy.md":
        ['reviews'],   # was ['justblogging']
    "2009-08-21-social-reference-manager-mendeley.md":
        ['research-analytics', 'reviews'],   # was ['digital-humanities', 'techlife']
    "2009-08-26-michael-nymans-concert.md":
        ['computermusic'],   # was ['justblogging']
    "2009-09-11-weird-example-com-urls-appearing-on-my-django-site.md":
        ['reviews'],   # was ['techlife']
    "2009-09-13-learning-iphone-development-while-sitting-on-your-couch.md":
        ['reviews'],   # was ['justblogging']
    "2009-10-14-pong-screensaver.md":
        ['reviews'],   # was ['justblogging']
    "2009-10-20-uml-to-django.md":
        ['knowledge-engineering', 'techlife'],   # was ['knowledge-engineering']
    "2009-10-31-wittgensteins-tractatus.md":
        ['data-science', 'digital-humanities'],   # was ['digital-humanities']
    "2009-11-11-the-four-pillars-of-the-ethical-company.md":
        ['reviews'],   # was ['justblogging']
    "2009-12-02-echoing-freedoms-requests.md":
        ['reviews'],   # was ['justblogging']  # not in the review (in review or newer); placed by hand
    "2010-01-04-links-4110.md":
        ['reviews'],   # was ['justblogging']
    "2010-01-10-livecoding-night-kings-college-coming-up.md":
        ['computermusic'],   # was ['justblogging']
    "2010-01-28-apples-ipad-has-been-announced.md":
        ['reviews'],   # was ['justblogging']
    "2010-02-03-the-anti-internet-saga-continues.md":
        ['reviews'],   # was ['justblogging']
    "2010-02-14-musical-intermezzo.md":
        ['computermusic'],   # was ['justblogging']
    "2010-02-16-the-afterafterparty.md":
        ['reviews'],   # was ['justblogging']  # not in the review (in review or newer); placed by hand
    "2010-02-18-processing-js-iprocessing-javascript-does-everything-for-you.md":
        ['computermusic'],   # was ['techlife']
    "2010-03-05-bbc-article-on-interactive-art-at-goldsmith-university-london.md":
        ['computermusic'],   # was ['justblogging']
    "2010-03-09-japanese-figurative-paintings.md":
        ['computermusic'],   # was ['justblogging']
    "2010-03-11-tale-of-tales-artistic-interactive-games-from-belgium.md":
        ['computermusic'],   # was ['justblogging']
    "2010-03-23-victim-of-the-brain.md":
        ['digital-humanities'],   # was ['justblogging']
    "2010-03-25-links-to-cs-193p-iphone-dev-lectures.md":
        ['reviews'],   # was ['techlife']
    "2010-04-12-creativity-and-personal-mastery.md":
        ['reviews'],   # was ['justblogging']
    "2010-05-24-django-debug-toolbar.md":
        ['reviews'],   # was ['techlife']
    "2010-06-10-back-to-imovie-hd.md":
        ['reviews'],   # was ['justblogging']
    "2010-06-13-plork-spring-2010-concert.md":
        ['computermusic'],   # was ['justblogging']
    "2010-06-17-ozrics-back-on-the-road.md":
        ['computermusic'],   # was ['justblogging']
    "2010-06-29-il-fatto-quotidiano-online-is-available.md":
        ['reviews'],   # was ['justblogging']  # not in the review (in review or newer); placed by hand
    "2010-06-30-djangocon-europe-2010.md":
        ['reviews'],   # was ['techlife']
    "2010-07-05-gong-how-to-stay-alive-video-clip.md":
        ['computermusic'],   # was ['justblogging']  # not in the review (in review or newer); placed by hand
    "2010-07-13-bernsteins-mass-at-royal-festical-hall.md":
        ['computermusic'],   # was ['justblogging']
    "2010-07-13-space-invaders-for-iphone.md":
        ['reviews'],   # was ['computermusic']
    "2010-07-26-knowledge-representation-workshop-cch.md":
        ['digital-humanities', 'knowledge-engineering'],   # was ['knowledge-engineering']
    "2010-08-09-listen-to-the-rainforest-at-kew-gardens.md":
        ['computermusic'],   # was ['justblogging']
    "2010-08-10-learning-resources-about-scheme.md":
        ['computermusic', 'techlife'],   # was ['computermusic']
    "2010-09-08-ars-electronica-2010.md":
        ['computermusic'],   # was ['justblogging']
    "2010-09-15-the-bad-plus-iron-man.md":
        ['computermusic'],   # was ['justblogging']
    "2010-09-22-mapping-stereotypes.md":
        ['reviews'],   # was ['justblogging']
    "2010-10-07-mathematics-and-our-body.md":
        ['reviews'],   # was ['justblogging']
    "2010-10-14-amazons-kindle-is-slowly-changing-my-life.md":
        ['digital-humanities'],   # was ['digital-humanities', 'justblogging']
    "2010-10-15-gmail-labels-sorting-order.md":
        ['techlife'],   # was ['justblogging']
    "2010-10-17-this-tube-can-make-or-break-presidents-popes-prime-ministers.md":
        ['reviews'],   # was ['justblogging']
    "2010-10-28-jeff-beck-live-at-the-royal-albert-hall.md":
        ['computermusic'],   # was ['justblogging']
    "2010-10-29-a-video-that-may-convince-you-that-lispers-are-a-bit-crazy.md":
        ['reviews'],   # was ['computermusic']
    "2010-10-29-ozric-tentacles-live-islington-academy-london.md":
        ['computermusic'],   # was ['justblogging']
    "2010-11-08-scheme-and-lisp.md":
        ['techlife'],   # was ['computermusic']
    "2011-01-07-the-digital-story-of-nativity-and-other-inspiring-stuff.md":
        ['reviews'],   # was ['justblogging']
    "2011-01-07-working-toward-meritocracy-in-italy.md":
        ['reviews'],   # was ['justblogging']
    "2011-01-29-opening-a-finders-window-from-impromptu-alas-how-to-use-the-applescript-bridge.md":
        ['techlife'],   # was ['computermusic']
    "2011-02-24-survey-of-pythonic-tools-for-rdf-and-linked-data-programming.md":
        ['knowledge-engineering'],   # was ['knowledge-engineering', 'techlife']
    "2011-04-09-a-space-odyssey-live-with-philharmonia-orchestra.md":
        ['computermusic'],   # was ['justblogging']
    "2011-04-14-allegro-cl-graph.md":
        ['knowledge-engineering'],   # was ['knowledge-engineering', 'techlife']
    "2011-04-16-ether-festival.md":
        ['computermusic'],   # was ['justblogging']
    "2011-06-09-djfacet-a-django-faceted-browser.md":
        ['data-science', 'techlife'],   # was ['knowledge-engineering', 'techlife']
    "2011-06-26-bjork-redefines-the-musicians-product-with-biophilia-albumapp.md":
        ['computermusic'],   # was ['justblogging']
    "2011-06-29-livecoding-is-like-gardening.md":
        ['computermusic', 'reviews'],   # was ['computermusic']
    "2011-06-30-digital-humanities-conference-2011-a-short-review.md":
        ['digital-humanities', 'reviews'],   # was ['digital-humanities']
    "2011-07-08-livecoding-in-paris-stransbourg.md":
        ['computermusic'],   # was ['justblogging']
    "2011-09-02-getting-lost-in-the-world-of-laputa.md":
        ['reviews'],   # was ['justblogging']
    "2011-09-28-event-thatcamp-kansas-and-digital-humanities-forum.md":
        ['digital-humanities', 'reviews'],   # was ['digital-humanities']
    "2011-10-06-article-algorithmic-composition-computational-thinking-in-music.md":
        ['computermusic', 'reviews'],   # was ['computermusic']
    "2011-12-26-article-thought-and-performance-live-coding-music-explained-to-anyone.md":
        ['computermusic', 'reviews'],   # was ['computermusic']
    "2012-01-13-special-issue-of-cmj-dvd-on-livecoding.md":
        ['computermusic', 'reviews'],   # was ['computermusic']
    "2012-02-08-html5-canvas-cookbook.md":
        ['reviews'],   # was ['techlife']
    "2012-03-01-the-future-of-the-book.md":
        ['digital-humanities'],   # was ['digital-humanities', 'techlife']
    "2012-03-09-composing-at-the-metalevel.md":
        ['computermusic', 'reviews'],   # was ['computermusic']
    "2012-05-16-djfacet-0-9-7-mptt-hierarchical-facets-now-supported.md":
        ['techlife'],   # was ['knowledge-engineering']
    "2012-07-08-wittgenstein-and-the-javascript-infovis-toolkit.md":
        ['data-science', 'digital-humanities'],   # was ['digital-humanities']
    "2012-08-07-using-mendeley-and-dropbox-to-sync-your-pdf-library-across-computers.md":
        ['reviews'],   # was ['techlife']
    "2012-09-10-navigating-through-the-people-of-medieval-scotland.md":
        ['data-science', 'digital-humanities', 'knowledge-engineering'],   # was ['digital-humanities', 'knowledge-engineering']
    "2012-09-21-open-knowledge-festival-helsinki-18-22-september-2012.md":
        ['knowledge-engineering', 'reviews'],   # was ['knowledge-engineering']
    "2012-10-12-teaching-programming-concepts-visually-with-the-online-python-tutor.md":
        ['reviews'],   # was ['justblogging']
    "2013-01-16-2012-a-look-back.md":
        ['reviews'],   # was ['justblogging']
    "2013-02-27-agile-and-waterfall.md":
        ['reviews'],   # was ['justblogging']
    "2013-04-27-annual-bliss-classification-association-lecture-using-faceted-browsers-in-the-dh.md":
        ['digital-humanities'],   # was ['digital-humanities', 'justblogging']
    "2013-06-05-eswc-2013-report-from-the-conference.md":
        ['knowledge-engineering', 'reviews'],   # was ['knowledge-engineering']
    "2013-08-13-textmate-bundle-for-turtle-and-sparql.md":
        ['knowledge-engineering'],   # was ['knowledge-engineering', 'techlife']
    "2013-12-16-annotating-the-web-with-scrible.md":
        ['digital-humanities'],   # was ['digital-humanities', 'justblogging']
    "2014-08-22-visualising-a-big-taxonomy-in-a-small-screen-in-pure-html.md":
        ['data-science', 'knowledge-engineering'],   # was ['data-science']
    "2014-10-27-getting-started-with-a-triplestore-on-mac-os-cliopatria.md":
        ['knowledge-engineering'],   # was ['knowledge-engineering', 'techlife']
    "2014-11-25-iswc14-paper-a-hybrid-semantic-publishing-architecture-combining-xml-and-rdf.md":
        ['knowledge-engineering'],   # was ['research-analytics']
    "2014-12-03-dereference-a-doi-using-python.md":
        ['research-analytics', 'techlife'],   # was ['techlife']
    "2015-01-05-introducing-resquotes-com.md":
        ['digital-humanities'],   # was ['digital-humanities', 'justblogging']
    "2015-02-04-ruse-in-chains.md":
        ['computermusic'],   # was ['justblogging']
    "2015-04-30-nature-com-ontologies-portal-available-online.md":
        ['knowledge-engineering', 'research-analytics'],   # was ['research-analytics']
    "2015-09-21-another-experiment-with-wittgensteins-tractatus.md":
        ['data-science', 'digital-humanities'],   # was ['digital-humanities', 'knowledge-engineering']
    "2015-11-28-accessing-os-x-dictionary-with-python.md":
        ['techlife'],   # was ['justblogging', 'techlife']
    "2016-01-03-nature-com-subjects-stream-graph.md":
        ['data-science', 'research-analytics'],   # was ['research-analytics']
    "2016-04-29-spotisci-finding-science-concepts-on-spotify.md":
        ['research-analytics'],   # was ['justblogging', 'techlife']
    "2016-10-21-open-data-summit-2016.md":
        ['knowledge-engineering', 'research-analytics', 'reviews'],   # was ['research-analytics']
    "2017-02-27-ontospy-v-1-7-4.md":
        ['knowledge-engineering'],   # was ['knowledge-engineering', 'techlife']
    "2018-05-23-sn-scigraph-is-part-of-the-linked-open-data-cloud-2018.md":
        ['knowledge-engineering', 'research-analytics'],   # was ['research-analytics']
    "2018-08-01-sn-scigraph-latest-website-release-make-it-easier-to-discover-related-content.md":
        ['knowledge-engineering', 'research-analytics'],   # was ['research-analytics']
    "2018-11-23-exploring-scholarly-publications-via-dbpedia.md":
        ['knowledge-engineering', 'research-analytics'],   # was ['research-analytics']
    "2019-02-11-zero-hunger-hack-day.md":
        ['data-science', 'research-analytics'],   # was ['research-analytics']
    "2019-04-25-vscode-override-snippets.md":
        ['techlife'],   # was []
    "2019-05-03-running-jupyter-demos-via-mybinder-org.md":
        ['techlife'],   # was ['data-science']
    "2019-05-24-introducing-dimcli-a-python-cli-for-dimensions-api.md":
        ['data-science', 'research-analytics'],   # was ['data-science', 'research-analytics', 'techlife']
    "2019-06-30-pypapers-a-bare-bones-command-line-pdf-manager.md":
        ['research-analytics', 'techlife'],   # was ['digital-humanities', 'techlife']
    "2021-08-30-recordit-plugin.md":
        ['computermusic', 'techlife'],   # was ['computermusic']
    "2021-10-29-django-wget-static-site.md":
        ['techlife'],   # was []
    "2022-03-02-Three-things-i-like-about-looker.md":
        ['data-science', 'reviews'],   # was ['data-science']
    "2022-04-20-Three-things-i-do-not-like-about-looker.md":
        ['data-science', 'reviews'],   # was ['data-science']
    "2022-06-30-a-semi-automated-conference-assistant.md":
        ['research-analytics'],   # was ['research-analytics', 'techlife']
    "2022-10-30-Ontospy-v2-released.md":
        ['knowledge-engineering'],   # was ['techlife']
    "2023-01-19-introducing-paperpile.md":
        ['research-analytics', 'reviews'],   # was ['justblogging']
    "2023-06-05-chatgpt-as-music.md":
        ['knowledge-engineering'],   # was ['justblogging']
    "2023-07-01-deep-work.md":
        ['reviews'],   # was ['justblogging']
    "2024-09-27-open-alex-topics.md":
        ['data-science', 'research-analytics'],   # was ['data-science', 'knowledge-engineering', 'research-analytics']
    "2025-03-17-installation-sydney-data-arena.md":
        ['computermusic'],   # was ['justblogging']
    "2025-10-27-hayden-thorpe-live.md":
        ['computermusic'],   # was ['justblogging']
    "2026-03-03-shifting-landscape-research-analytics.md":
        ['research-analytics', 'reviews'],   # was ['research-analytics']
    "2026-04-21-funding-flows-global-south-clacso.md":
        ['research-analytics', 'reviews'],   # was ['research-analytics']
    "2026-06-16-ai-skills-cottage-industry.md":
        ['knowledge-engineering'],   # was ['techlife']
    "2026-08-17-five-new-ways-to-read-the-tractatus.md":
        ['data-science', 'digital-humanities'],   # was ['digital-humanities']
    "2026-09-02-reading-naples-44-as-a-database.md":
        ['data-science', 'digital-humanities'],   # was ['digital-humanities']
    "2026-09-10-a-dream-of-venice.md":
        ['data-science'],   # was ['justblogging']
    "2026-10-11-the-mom-test.md":
        ['reviews'],   # was ['techlife']
    "2026-10-12-ontospy-three-releases-in-a-day.md":
        ['knowledge-engineering'],   # was ['techlife']
    "2026-11-13-quiver-dont-quake.md":
        ['reviews'],   # was ['techlife']  # not in the review (in review or newer); placed by hand
}
