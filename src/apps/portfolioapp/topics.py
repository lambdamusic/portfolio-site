"""
The topics structure used in the homepage visualization

Case: as in final rendering
Top level has None as key

Each topic, eventually, must have a unique key 
"""


# struct used to determine links and position in tree // parent : children
topics = {
    "TOP": 
        ["Knowledge Modeling", "Web Development", "Data Science"], 
    "Knowledge Modeling" : 
        ['Ontology', "Knowledge Graphs", "Data Architecture", "Epistemology", "Information Architecture", "Lisp"], 
    "Web Development" : 
        ['Python', "Django",  "Html/CSS", "Information Architecture", "Data Architecture", "Faceted Search", ], 
    "Data Science" : 
        ['Python', "Data Visualization", "Plotly", "Jupyter Notebooks", "Data Architecture", "Exploratory Data Analysis"], 
    "Knowledge Graphs" : 
        ["RDF", "Linked Data", ], 
    "Data Architecture" : 
        ["APIs", "Relational DBs", "NoSQL", "Knowledge Graphs"], 
}


top_topics = topics["TOP"]

# create unique list of nodes / only from CHILDREN 
topics_unique = set()
for x in topics:
    for a in topics[x]:
        topics_unique.add(a)

# explode links into tuples
topics_links = set()
for x in topics:
    for a in topics[x]:
        topics_links.add((x, a))