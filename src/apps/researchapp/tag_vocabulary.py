"""
The controlled tag vocabulary for blog posts and projects.

Markdown frontmatter is the source of truth for tags (see TAGS_PLAN.md);
this module is the dictionary that says which tag names are legitimate and
what every historical variant folds into.

Three structures:

    VOCABULARY   canonical tag -> facet        the allowed list
    ALIASES      variant -> canonical          what to rewrite
    DROP         tags to delete outright       long-tail noise

Used by:
    manage.py tags_audit    reports conformance against this file
    manage.py tags_apply    rewrites the markdown frontmatter to match

CONVENTIONS (decided 2026-09-22)
    - lowercase
    - hyphen-separated for multi-word terms: `digital-humanities`, not
      `digitalhumanities`
    - singular nouns: `book`, `event`, `tutorial`
    - deliberate exceptions, because they are terms of art written as one
      word in their own communities: `livecoding`, `web2` (folded into
      `social-web`), `macos`, `nlp`, `ai`, `ui`, `hci`, `pdf`, `rdf`, `owl`

FACETS
    domain  broad subject area - the "what is this about" layer
    tech    a concrete technology, language, tool or platform
    format  what kind of thing the post/project *is* (or produced)
    topic   everything else worth navigating by: people, places, concepts
"""

# --------------------------------------------------------------------------
# VOCABULARY - the canonical list. Anything not here is an error.
# --------------------------------------------------------------------------

VOCABULARY = {
    # -- domain ------------------------------------------------------------
    "ai": "domain",
    "cognitive-science": "domain",
    "data-science": "domain",
    "digital-humanities": "domain",
    "information-architecture": "domain",
    "knowledge-representation": "domain",
    "linked-data": "domain",
    "livecoding": "domain",
    "nlp": "domain",
    "ontology": "domain",
    "philosophy": "domain",
    "programming": "domain",
    "research-analytics": "domain",
    "semantic-web": "domain",

    # -- tech --------------------------------------------------------------
    "api": "tech",
    "d3": "tech",
    "database": "tech",
    "django": "tech",
    "extempore": "tech",
    "graph": "tech",
    "html5": "tech",
    "ide": "tech",
    "impromptu": "tech",
    "ios": "tech",
    "javascript": "tech",
    "jupyter": "tech",
    "lisp": "tech",
    "macos": "tech",
    "owl": "tech",
    "pdf": "tech",
    "processing": "tech",
    "python": "tech",
    "rdf": "tech",
    "scheme": "tech",
    "sparql": "tech",
    "terminal": "tech",
    "triplestore": "tech",
    "version-control": "tech",
    "xml": "tech",

    # -- format ------------------------------------------------------------
    "book": "format",
    "conference": "format",
    "dashboard": "format",
    "documentation": "format",
    "event": "format",
    "movie": "format",
    "news": "format",
    "paper": "format",
    "quote": "format",
    "talk": "format",
    "tool": "format",
    "tutorial": "format",
    "video": "format",
    "website": "format",

    # -- topic -------------------------------------------------------------
    "academia": "topic",
    "algorithmic-composition": "topic",
    "annotation": "topic",
    "art": "topic",
    "blog": "topic",
    "browser": "topic",
    "citation": "topic",
    "classical": "topic",
    "composition": "topic",
    "creativity": "topic",
    "dimensions": "topic",
    "electronica": "topic",
    "europe": "topic",
    "faceted-search": "topic",
    "google": "topic",
    "graphics": "topic",
    "guitar": "topic",
    "hci": "topic",
    "history": "topic",
    "italy": "topic",
    "japan": "topic",
    "language": "topic",
    "learning": "topic",
    "live-performance": "topic",
    "logic": "topic",
    "london": "topic",
    "modeling": "topic",
    "music": "topic",
    "nature": "topic",
    "navigation": "topic",
    "ontospy": "topic",
    "open-data": "topic",
    "philosurfical": "topic",
    "politics": "topic",
    "productivity": "topic",
    "publishing": "topic",
    "research": "topic",
    "rock": "topic",
    "science": "topic",
    "scigraph": "topic",
    "search": "topic",
    "semantics": "topic",
    "social-web": "topic",
    "synth": "topic",
    "taxonomy": "topic",
    "travel": "topic",
    "tree": "topic",
    "ui": "topic",
    "visualization": "topic",
    "web": "topic",
    "wittgenstein": "topic",
}


# --------------------------------------------------------------------------
# ALIASES - variant -> canonical. Applied to the markdown frontmatter.
# Grouped by target, so the intent of each merge stays readable.
# --------------------------------------------------------------------------

ALIASES = {
    # ---- spelling / plural variants (the mechanical ones) ----------------
    "semanticweb": "semantic-web",
    "linkeddata": "linked-data",
    "digitalhumanities": "digital-humanities",
    "cognitivescience": "cognitive-science",
    "algorithmiccomposition": "algorithmic-composition",
    "opendata": "open-data",
    "books": "book",
    "events": "event",
    "tutorials": "tutorial",
    "quotes": "quote",
    "movies": "movie",
    "languages": "language",
    "representations": "knowledge-representation",
    "representation": "knowledge-representation",
    "urls": "web",
    "url": "web",
    "tools": "tool",
    "d3-js": "d3",

    # ---- ai --------------------------------------------------------------
    "artificial-intelligence": "ai",
    "llm": "ai",
    "chatgpt": "ai",
    "eliza": "ai",

    # ---- cognitive-science ----------------------------------------------
    "brain": "cognitive-science",
    "mind": "cognitive-science",
    "embodied": "cognitive-science",
    "body": "cognitive-science",
    "cybernetics": "cognitive-science",
    "bateson": "cognitive-science",
    "maturana": "cognitive-science",
    "systems": "cognitive-science",
    "signals": "cognitive-science",

    # ---- data-science ----------------------------------------------------
    "data": "data-science",
    "statistics": "data-science",
    "analysis": "data-science",
    "data-exploration": "data-science",

    # ---- digital-humanities ---------------------------------------------
    "digital-history": "digital-humanities",
    "humanities-computing": "digital-humanities",

    # ---- information-architecture ---------------------------------------
    "ia": "information-architecture",
    "information-exploration": "information-architecture",
    "knowledgemanagement": "information-architecture",

    # ---- knowledge-representation ---------------------------------------
    "kr": "knowledge-representation",
    "knowledge": "knowledge-representation",
    "symbol": "knowledge-representation",
    "metadata": "knowledge-representation",

    # ---- research-analytics ---------------------------------------------
    "scientometrics": "research-analytics",
    "researchanalytics": "research-analytics",
    "scholarly-analytics": "research-analytics",

    # ---- semantic-web / linked-data / rdf --------------------------------
    "schema-org": "semantic-web",
    "dbpedia": "linked-data",
    "lod-cloud": "linked-data",
    "turtle": "rdf",
    "jsonld": "rdf",
    "rdflib": "rdf",
    "skos": "owl",
    "stardog": "triplestore",
    "cliopatria": "triplestore",

    # ---- ontology / modeling --------------------------------------------
    "dolce": "ontology",
    "hozo": "ontology",
    "cidoc": "ontology",
    "frbr": "ontology",
    "frbr-oo": "ontology",
    "metamodel": "modeling",
    "uml": "modeling",
    "argouml": "modeling",
    "stereotype": "modeling",

    # ---- python / django -------------------------------------------------
    "macpython": "python",
    "easy_install": "python",
    "pil": "python",
    "pysmell": "python",
    "urllib": "python",
    "pdb": "python",
    "idle": "python",
    "scraping": "python",
    "djangodoc": "django",
    "q_objects": "django",
    "admin": "django",
    "webapp": "django",
    "mptt": "tree",

    # ---- other languages / general programming ---------------------------
    "clojure": "lisp",
    "macro": "lisp",
    "functional": "lisp",
    "taube": "lisp",
    "jquery": "javascript",
    "html": "html5",
    "canvas": "html5",
    "code": "programming",
    "software": "programming",
    "debug": "programming",
    "bug": "programming",
    "java": "programming",
    "ruby": "programming",
    "php": "programming",
    "objc": "programming",
    "flash": "programming",
    "flex": "programming",

    # ---- platforms / tooling ---------------------------------------------
    "mac": "macos",
    "osx": "macos",
    "apple": "macos",
    "leopard": "macos",
    "lion": "macos",
    "finder": "macos",
    "applescript": "macos",
    "screensaver": "macos",
    "fluid": "macos",
    "backlight": "macos",
    "iphone": "ios",
    "ipad": "ios",
    "mobile": "ios",
    "textmate": "ide",
    "editor": "ide",
    "emacs": "ide",
    "cli": "terminal",
    "shell": "terminal",
    "snippets": "terminal",
    "git": "version-control",
    "github": "version-control",
    "svn": "version-control",
    "subversion": "version-control",
    "mercurial": "version-control",
    "versioncontrol": "version-control",
    "gist": "version-control",
    "notebooks": "jupyter",
    "googlecolab": "jupyter",
    "gae": "google",
    "hydra": "api",

    # ---- data stores -----------------------------------------------------
    "db": "database",
    "mysql": "database",
    "mysqldb": "database",
    "bigtable": "database",
    "neo4j": "graph",
    "network": "graph",
    "pygraph": "graph",
    "markup": "xml",

    # ---- search / IA / UI -------------------------------------------------
    "elasticsearch": "search",
    "kibana": "search",
    "query": "search",
    "faceted": "faceted-search",
    "autocomplete": "faceted-search",
    "autocompletion": "faceted-search",
    "pathways": "navigation",
    "hypertext": "navigation",
    "interface": "ui",
    "gui": "ui",
    "uif": "ui",
    "userstudy": "hci",
    "questionnaire": "hci",
    "tagging": "annotation",
    "label": "annotation",

    # ---- visual ----------------------------------------------------------
    "infographics": "visualization",
    "flare": "d3",
    "opengl": "graphics",
    "quartzcomposer": "graphics",
    "svg": "graphics",
    "image": "graphics",
    "flickr": "graphics",
    "digitalart": "art",
    "drawing": "art",
    "painting": "art",
    "sculpture": "art",
    "museum": "art",
    "installation": "art",

    # ---- music -----------------------------------------------------------
    "audio": "music",
    "sound": "music",
    "song": "music",
    "mp3": "music",
    "spotify": "music",
    "jamendo": "music",
    "player": "music",
    "jazz": "music",
    "blues": "music",
    "progrock": "rock",
    "space-rock": "rock",
    "stoner-rock": "rock",
    "psychedelic": "rock",
    "blacksabbath": "rock",
    "ozrics": "rock",
    "alice-in-chains": "rock",
    "beck": "rock",
    "aphextwin": "electronica",
    "eno": "electronica",
    "ikeda": "electronica",
    "noise": "electronica",
    "minimalism": "electronica",
    "bach": "classical",
    "bernstein": "classical",
    "serialism": "classical",
    "mass": "classical",
    "propellerhead": "synth",
    "audiounit": "synth",
    "sequencer": "synth",
    "reaper": "synth",
    "lilypond": "composition",
    "sheetmusic": "composition",
    "notation": "composition",
    "composing": "composition",
    "progression": "composition",
    "live": "live-performance",
    "performance": "live-performance",
    "concert": "live-performance",
    "gigs": "live-performance",

    # ---- film / media ----------------------------------------------------
    "film": "movie",
    "documentary": "movie",
    "dvd": "movie",
    "kubrick": "movie",
    "horror": "movie",
    # `television` folded into `movie`: only 2 posts, and both are about
    # screen narrative rather than broadcast as such.
    "television": "movie",
    "anime": "movie",
    "cartoon": "movie",
    "screencast": "video",
    "quicktime": "video",
    "imovie": "video",

    # ---- formats / events -------------------------------------------------
    "eswc": "conference",
    "thatcamp": "conference",
    "workshop": "conference",
    "hackday": "conference",
    "registration": "conference",
    "festival": "event",
    "presentation": "talk",
    "slides": "talk",
    "article": "paper",
    "reference": "documentation",
    "cheatsheet": "tutorial",
    "tips": "tutorial",
    "trick": "tutorial",
    "bbc": "news",
    "looker": "dashboard",
    "dash": "dashboard",
    "analytics": "dashboard",

    # ---- reading / publishing --------------------------------------------
    "ebook": "book",
    "kindle": "book",
    "reading": "book",
    "press": "publishing",
    "journal": "publishing",
    "doi": "citation",
    "bibliography": "citation",
    "zotero": "citation",
    "mendeley": "citation",
    "reference_manager": "citation",

    # ---- language / logic / philosophy ------------------------------------
    "text": "nlp",
    "text-analysis": "nlp",
    "parsing": "nlp",
    "spellchecking": "nlp",
    "linguistics": "language",
    "dictionary": "language",
    "latin": "language",
    "bengali": "language",
    "collation": "language",
    "argumentation": "logic",
    "mathematics": "logic",
    "theory": "logic",
    "epistemology": "philosophy",
    "ethics": "philosophy",

    # ---- web / social -----------------------------------------------------
    "web2": "social-web",
    "social": "social-web",
    "sharing": "social-web",
    "crowdsourcing": "social-web",
    "collaboration": "social-web",
    "delicious": "social-web",
    "wikipedia": "social-web",
    "links": "social-web",
    "internet": "web",
    "online": "web",
    "static": "web",
    "cms": "web",
    "intranet": "web",
    "chrome": "browser",
    "rss": "blog",
    "open": "open-data",

    # ---- work / self --------------------------------------------------------
    "inspiration": "creativity",
    "ideas": "creativity",
    "mindmapping": "creativity",
    "work": "productivity",
    "agile": "productivity",
    "waterfall": "productivity",
    "project": "productivity",
    "self-improvement": "productivity",
    "zen": "productivity",

    # ---- places / institutions ---------------------------------------------
    "naples": "italy",
    "venice": "italy",
    "paris": "europe",
    "strasbourg": "europe",
    "helsinki": "europe",
    "linz": "europe",
    "austria": "europe",
    "places": "travel",
    "australia": "travel",
    "newzealand": "travel",
    "india": "travel",
    "kansas": "travel",
    "academic": "academia",
    "phd": "academia",
    "university": "academia",
    "ucl": "academia",
    "stanford": "academia",
    "princeton": "academia",
    "goldsmith": "academia",
    "lab": "academia",
    "discipline": "academia",
    "mit": "academia",
    "ou": "academia",
    "elearning": "learning",
    "education": "learning",
    "teaching": "learning",
    "skills": "learning",

    # ---- history ------------------------------------------------------------
    "archeology": "history",
    "classics": "history",
    "medieval": "history",

    # ---- politics ------------------------------------------------------------
    "society": "politics",
    "meritocracy": "politics",
    "transparency": "politics",
    "law": "politics",
    "open-democracy": "politics",
}


# --------------------------------------------------------------------------
# DROP - deleted outright. One-off tags with no canonical home: too specific
# to navigate by, too vague to mean anything, or simply not about the post.
# --------------------------------------------------------------------------

DROP = {
    "adaptation", "app", "art-nouveau", "bands", "bookmarklet", "chm",
    "comparison", "culture", "design", "dynamic", "earthquake", "email",
    "free", "funny", "games", "gardens", "gis", "gmail", "ichat", "ims",
    "interactive",
    "kali", "keyboard", "laptop", "latency", "map", "marimba", "media",
    "metronome", "msn", "multimedia", "narrative", "digitalnarrative",
    "patch", "pitfall", "play",
    "podcast", "satire", "settings", "smtp", "smtpd", "storyteller", "tagore",
    "technology", "television-uk", "tropical", "uk", "volume", "zebra",
}


# Explicit tag assignment for individual posts. Used for the 32 posts that
# had no tags at all (mostly 2006-2007, written before I was tagging), where
# there is nothing to map from - the tags were read off the post content.
# Wins over ALIASES/DROP, and a tags: block is created if the post lacks one.
POST_TAGS = {
    "2006-04-06-library-20.md":
        ['learning', 'social-web', 'talk'],
    "2006-10-04-navigating-the-rijksmuseum.md":
        ['art', 'navigation', 'ui'],
    "2006-10-09-howar-gardners-talk.md":
        ['academia', 'cognitive-science', 'talk'],
    "2006-10-23-semantic-wikipedia-some-issues.md":
        ['semantic-web', 'social-web', 'talk'],
    "2006-10-28-firefox-20-will-i-ever-go-back-to-safari.md":
        ['browser', 'macos'],
    "2006-10-29-132.md":
        ['academia', 'quote'],
    "2006-11-21-web-30.md":
        ['news', 'semantic-web', 'web'],
    "2006-11-23-multimedian-semantic-navigator.md":
        ['art', 'navigation', 'semantic-web'],
    "2006-11-28-the-nora-project.md":
        ['digital-humanities', 'language', 'nlp'],
    "2006-11-30-knowledge-elicitation-playing-with-cards.md":
        ['knowledge-representation', 'research'],
    "2006-12-01-a-cyberspace-atlas.md":
        ['graphics', 'visualization'],
    "2006-12-06-lisp-and-the-web.md":
        ['lisp', 'programming', 'web'],
    "2007-01-05-text-encoding-initiative-a-historical-paper.md":
        ['digital-humanities', 'paper', 'xml'],
    "2007-01-17-where-is-italy.md":
        ['italy', 'politics', 'visualization'],
    "2007-01-18-the-internet-classics-archive.md":
        ['book', 'digital-humanities', 'history'],
    "2007-01-24-google-map-goes-down-to-the-humans.md":
        ['event', 'google'],
    "2007-01-26-turning-the-pages-of-literature.md":
        ['book', 'digital-humanities', 'ui'],
    "2007-02-01-philosophical-search-engine.md":
        ['academia', 'philosophy', 'search'],
    "2007-02-06-lisp-conference-in-cambridge.md":
        ['conference', 'lisp'],
    "2007-03-19-navigating-the-eternal-egypt.md":
        ['art', 'digital-humanities', 'history', 'navigation'],
    "2007-03-22-digital-document-quarterly.md":
        ['digital-humanities', 'publishing', 'semantics'],
    "2007-04-02-indiana-philosophy-ontology-project.md":
        ['digital-humanities', 'ontology', 'philosophy', 'wittgenstein'],
    "2007-04-17-hypernietzsche.md":
        ['digital-humanities', 'navigation', 'philosophy'],
    "2007-04-19-carnap-on-syntax.md":
        ['language', 'logic', 'philosophy'],
    "2007-05-12-impromptu-scheme-based-music-and-video.md":
        ['impromptu', 'livecoding', 'scheme'],
    "2007-05-31-go-get-the-milk.md":
        ['graphics', 'video'],
    "2009-08-01-end-of-this-adventure.md":
        ['academia', 'london'],
    "2018-03-22-interesting-read-scisci-i-e-the-science-of-science.md":
        ['graph', 'paper', 'research-analytics', 'science'],
    "2019-02-11-zero-hunger-hack-day.md":
        ['dashboard', 'dimensions', 'research-analytics', 'visualization'],
    "2019-04-25-vscode-override-snippets.md":
        ['extempore', 'ide', 'tutorial'],
    "2020-01-08-calculating-industry-collaborations-via-grid.md":
        ['dimensions', 'research-analytics', 'tutorial', 'visualization'],
    "2021-10-29-django-wget-static-site.md":
        ['django', 'python', 'tutorial', 'website'],
}
