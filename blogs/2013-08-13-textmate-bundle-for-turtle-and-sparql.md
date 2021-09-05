---
title: "Textmate bundle for Turtle and Sparql"
date: "2013-08-13"
categories: 
  - "semantic-web"
  - "techlife"
tags: 
  - "semanticweb"
  - "sparql"
  - "textmate"
  - "turtle"
---

I recently ran into the Textmate [bundle for Turtle](https://github.com/peta/turtle.tmbundle), an extension for the [Textmate](https://github.com/textmate/textmate) osx editor aimed at facilitating working with RDF and SPARQL. If you happen to be using these technologies, well I'd suggest you take a look at the following post.

The Resource Description Framework is a _general-purpose language for representing information_ which is widely used on the web in order to encode metadata in a machine-interoperable format.

Turtle, the [terse RDF Triple Language](http://www.w3.org/TeamSubmission/turtle/), is a textual syntax for RDF which aims at human readability and compactness (among other things). This is what it looks like:

```

@prefix rdf: 
@prefix rdfs: 
@prefix xsd: .
@base 

:MotorVehicle a rdfs:Class.

:PassengerVehicle a rdfs:Class;
   rdfs:subClassOf :MotorVehicle.

:Person a rdfs:Class.

xsd:integer a rdfs:Datatype.

:registeredTo a rdf:Property;
   rdfs:domain :MotorVehicle;
   rdfs:range  :Person.

:myLittleCar a PassengerVehicle
```

The termite library in question, in a nutshell, provides a bunch of snippets and query mechanisms that make it easier to work with Turtle RDF and related technologies. More precisely, here's the official features breakdown:

> - Language grammar for Turtle and SPARQL 1.1
> - Powerful (!) auto-completion (live-aggregated)
> - Documentation for classes and roles/properties at your fingertips (live-aggregated)
> - Interactive SPARQL query scratchpad
> - Some snippets (prefixes and document skeleton)
> - Solid syntax validation
> - Commands for instant graph visualization of a knowledge base (requires [Graphviz](http://www.graphviz.org/) and [Raptor](http://librdf.org/raptor/))
> - Conversion between all common RDF formats

### Example

In order to query a SPARQL endpoint (eg DBPedia) just type this in and run it (apple-R):

```

#QUERY <http://dbpedia.org/sparql>                    
SELECT DISTINCT ?s ?label                             
WHERE {                                               
    ?s <http://dbpedia.org/property/season> ?o .      
}  
```

Obviously you can query any endpoint, e.g. [data.nature.com](http://data.nature.com/query):

```


#QUERY <http://data.nature.com/sparql>

PREFIX bibo:<http://purl.org/ontology/bibo/>
PREFIX dc:<http://purl.org/dc/elements/1.1/>
PREFIX dcterms:<http://purl.org/dc/terms/>
PREFIX foaf:<http://xmlns.com/foaf/0.1/>
PREFIX npg:<http://ns.nature.com/terms/>
PREFIX npgg:<http://ns.nature.com/graphs/>
PREFIX npgx:<http://ns.nature.com/extensions/>
PREFIX owl:<http://www.w3.org/2002/07/owl#>
PREFIX prism:<http://prismstandard.org/namespaces/basic/2.1/>
PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
PREFIX sc:<http://purl.org/science/owl/sciencecommons/>
PREFIX skos:<http://www.w3.org/2004/02/skos/core#>
PREFIX void:<http://rdfs.org/ns/void#>
PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>


SELECT *                            
WHERE {                                                
    ?doi a npg:Article . 
    ?doi dc:title ?title .
    ?doi prism:publicationDate ?date
} 
limit 100 

```

And this is just the tip of the iceberg. Autocompletion, visualisations etc… it may be the Textmate-Semantic Web swiss army knife you've been looking for.

![](/media/static/blog_img/screenshot-editor.png)

![](/media/static/blog_img/screenshot-sparql.png)

![](/media/static/blog_img/screenshot-visu.png)
