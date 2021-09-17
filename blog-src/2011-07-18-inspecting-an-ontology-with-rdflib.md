---
title: "Inspecting an ontology with RDFLib"
date: "2011-07-18"
categories: 
  - "semantic-web"
  - "techlife"
tags: 
  - "ontology"
  - "owl"
  - "rdf"
  - "rdflib"
---

RDFLib ([homepage](http://www.rdflib.net/)) is a pretty solid and comprehensive rdf-programming kit for Python. In a [previous post](http://www.michelepasin.org/blog/2011/02/24/survey-of-pythonic-tools-for-rdf-and-linked-data-programming/) I already discussed what pythonic options are currently available out there for doing semantic web programming; after some more in depth testing I realized that Rdflib is the most accessible and complete of them all (in fact many of the available libraries are based on Rdflib's APIs). So.. here we go: in this post I'm giving an overview of some of the things you can do with this library.

_**Update 2014-10-04**: the latest version of the Python library described in this post is available on [GitHub](https://github.com/lambdamusic/ontosPy)_

The [Linked Data](http://linkeddata.org/) world is _primarily_ made up of [RDF](http://en.wikipedia.org/wiki/Resource_Description_Framework), many would say, so the most important thing is being able to parse and extract information from this simple but versatile language. A quite well known mantra in this community is the '[a little semantics goes a long way](http://www.cs.rpi.edu/~hendler/LittleSemanticsWeb.html)', which expresses succinctly the idea that there's no need to fixate on the construction of large-scale [CYC](http://en.wikipedia.org/wiki/Cyc)\-like knowledge-based systems in order to get something going in an open-world scenario such as the web (of data).

In other words, this idea suggests that (for now) it's enough to make your application spit out structured data using a standard data model (RDF, that is), and possibly connect your RDF dataset to other datasets in the '[cloud](http://richard.cyganiak.de/2007/10/lod/)' by creating [rdf-links](http://linkeddatabook.com/editions/1.0/#htoc18). Once you've done that, you can take it easy and stop worrying about the data integration problems your RDF might generate, or the 'big picture'. Others will figure out how to use your data; **it's an incremental approach**, there will be some sort of snowball effect at some stage, semantic web enthusiasts seem to suggest. This and other arguments are a bit make-believe, I have to say; but at the same time they also do make some sense: unless we have some real stuff to play with out there on the data-web, not much will _ever_ happen!

### Hullo, RDFlib

After quickly ascertaining that it's not a total waste of time to work with RDF, it's now time to get practical and experiment a bit with RDFlib. This is a great python library for it lets you process RDF data _very very easily_. Example:

	
`# open a graph >>> import rdflib >>> graph = rdflib.Graph()  # load some data >>> graph.parse('http://dbpedia.org/resource/Semantic_Web') )> >>> len(graph) 98  # query the data >>> list(graph)[:10] [(rdflib.term.URIRef('http://dbpedia.org/resource/SUPER'), rdflib.term.URIRef('http://dbpedia.org/property/keywords'), rdflib.term.URIRef('http://dbpedia.org/resource/Semantic_Web')), (rdflib.term.URIRef('http://dbpedia.org/resource/Semantic_internet'), rdflib.term.URIRef('http://dbpedia.org/ontology/wikiPageRedirects'), rdflib.term.URIRef('http://dbpedia.org/resource/Semantic_Web')), (rdflib.term.URIRef('http://dbpedia.org/resource/SW'), rdflib.term.URIRef('http://dbpedia.org/ontology/wikiPageDisambiguates'), rdflib.term.URIRef('http://dbpedia.org/resource/Semantic_Web')), (rdflib.term.URIRef('http://dbpedia.org/resource/Semantic_integrity'), rdflib.term.URIRef('http://dbpedia.org/ontology/wikiPageRedirects'), rdflib.term.URIRef('http://dbpedia.org/resource/Semantic_Web')), (rdflib.term.URIRef('http://dbpedia.org/resource/Ontotext'), rdflib.term.URIRef('http://dbpedia.org/ontology/industry'), rdflib.term.URIRef('http://dbpedia.org/resource/Semantic_Web')), (rdflib.term.URIRef('http://mpii.de/yago/resource/Semantic_Web'), rdflib.term.URIRef('http://www.w3.org/2002/07/owl#sameAs'), rdflib.term.URIRef('http://dbpedia.org/resource/Semantic_Web')), (rdflib.term.URIRef('http://dbpedia.org/resource/Deborah_McGuinness'), rdflib.term.URIRef('http://dbpedia.org/ontology/knownFor'), rdflib.term.URIRef('http://dbpedia.org/resource/Semantic_Web')), (rdflib.term.URIRef('http://dbpedia.org/resource/The_semantic_web'), rdflib.term.URIRef('http://dbpedia.org/ontology/wikiPageRedirects'), rdflib.term.URIRef('http://dbpedia.org/resource/Semantic_Web')), (rdflib.term.URIRef('http://dbpedia.org/resource/Access-eGov'), rdflib.term.URIRef('http://dbpedia.org/property/keywords'), rdflib.term.URIRef('http://dbpedia.org/resource/Semantic_Web')), (rdflib.term.URIRef('http://dbpedia.org/resource/SOA4All'), rdflib.term.URIRef('http://dbpedia.org/property/keywords'), rdflib.term.URIRef('http://dbpedia.org/resource/Semantic_Web'))]  # print out some triples >>> for s, p, o in graph: ...     print s, "n--- ", p, "n------ ", o ...  http://dbpedia.org/resource/SUPER --- http://dbpedia.org/property/keywords  ------ http://dbpedia.org/resource/Semantic_Web http://dbpedia.org/resource/Semantic_internet --- http://dbpedia.org/ontology/wikiPageRedirects  ------ http://dbpedia.org/resource/Semantic_Web http://dbpedia.org/resource/SW --- http://dbpedia.org/ontology/wikiPageDisambiguates  ------ http://dbpedia.org/resource/Semantic_Web http://dbpedia.org/resource/Semantic_integrity --- http://dbpedia.org/ontology/wikiPageRedirects  ------ http://dbpedia.org/resource/Semantic_Web http://dbpedia.org/resource/Semantic_Web  --- http://dbpedia.org/ontology/abstract  ------ Con il termine web semantico, termine coniato dal suo ideatore, Tim Berners-Lee, si intende la trasformazione del World Wide Web in un ambiente dove i documenti pubblicati (pagine HTML, file, immagini, e così via) siano associati ad informazioni e dati che ne specifichino il contesto semantico in un formato adatto all'interrogazione, all'interpretazione e, più in generale, all'elaborazione automatica. Con l'interpretazione del contenuto dei documenti che il Web Semantico propugna, saranno possibili ricerche molto più evolute delle attuali, basate sulla presenza nel documento di parole chiave, ed altre operazioni specialistiche come la costruzione di reti di relazioni e connessioni tra documenti secondo logiche più elaborate del semplice link ipertestuale. http://dbpedia.org/resource/Semantic_Web  --- etc. etc etc................`

Pretty straightforward uh? In a nutshell, what we've just done is:  
**a)** loading the RDF description of the 'Semantic Web' page on [DBPedia](http://dbpedia.org/About) (http://dbpedia.org/resource/Semantic\_Web); **b)** showing the first 10 triples in that RDF graph; **c)** iterating through all the triples in the graph and printing them out in a format that reflects the subject-predicate-object structure of RDF.

**However we still don't know much about those data**. Meaning: what is the abstract structure used to define them? Do they conform to some sound and thorough data-model or is it just some automatically-generated messy agglomerate of database records? In other words, what I want to know is, what's the [ontology](http://en.wikipedia.org/wiki/Ontology_(information_science)) behind these data? How can I see it? Shall I reuse it (and thus endorse it) within my own application, or does my application require something slightly different?

I'm probably biased here, cause I personally get much more satisfaction from creating and thinking about ontologies rather than fiddling with large quantities of rdf-xml triples. Still, **I think that being able to evaluate the ontology a bunch of rdf refers to is of vital importance**, in order to judge whether that RDF is what you're looking for or not, and how to best integrate it in your application.

**Long story short, I couldn't find anything in RdfLib that would let me print out the hierarchy tree** of an ontology and other related information. So I thought, here's a good candidate-task for me to learn how to use the library better.

### Inspecting an ontology using RDFLib

I created a small class called '**OntoInspector**' that you can instantiate with an RDFS/OWL ontology and then query to find out basic information about that ontology. I know - all of this could have been done using one of the many (and constantly increasing) ontology editing tools - but hey this is all about learning isn't it? You can find all the source code on BitBucket [GitHub](https://github.com/lambdamusic/ontosPy). Feel free to get it and modify as needed. Also, I integrated this python toolkit within a **django application** that let you browse ontologies online (beware - it's just a hack really). This is called (surprise) **OntoView**, and it's [accessible here](http://www.michelepasin.org/hacks/ontoview/).

The first thing to do in our class definition is (obviously) loading up the RDFLib library. I've developed this using RDFlib 2.4, but recently tested it with 3.0 (the latest release available) and it all still works fine. By loading up the RDF and RDFS modules we'll have access to all the constants needed to query for classes and subclasses. Note that I added an OWL module as that is not part of RDFLib. You can find it in the source code, it's just a list of all predicates in the [OWL vocabulary](http://www.w3.org/TR/owl-guide/).

	`from rdflib import ConjunctiveGraph, Namespace, exceptions  from rdflib import URIRef, RDFS, RDF, BNode  import OWL`

Now let's set up the basic structure of the OntoInspector class. In principle, an OntoInspector object should contain all the information necessary to query an ontology. An ontology is referred to using its URI, so that's all is needed for creating an instance of OntoInspector too:

```
class OntoInspector(object):

    """Class that includes methods for querying an RDFS/OWL ontology"""        

    def __init__(self, uri, language=""):
        super(OntoInspector, self).__init__()

        self.rdfGraph = ConjunctiveGraph()
        try:
            self.rdfGraph.parse(uri, format="xml")
        except:
            try:
                self.rdfGraph.parse(uri, format="n3")
            except:
                raise exceptions.Error("Could not parse the file! Is it a valid RDF/OWL ontology?")

        finally:
            # let's cache some useful info for faster access
            self.baseURI = self.get_OntologyURI() or uri            
            self.allclasses = self.__getAllClasses(classPredicate)
            self.toplayer = self.__getTopclasses()
            self.tree = self.__getTree()


    def get_OntologyURI(self, ....):
        # todo
        pass

    def __getAllClasses(self, ....):
        # todo
        pass
       

    def __getTopclasses(self, ....):
        pass


    def __getTree(self, ....):
        # todo
        pass
```

As you can see the \_\_init\_\_ method tries to load the ontology file (which can be expressed in either rdf/xml or n3 format) and then sets up 4 class attributes. These attributes will contain some key information about the ontology: its **URI**, a list of **all the classes** available, the classes in the **top layer** and the main **taxonomical tree** of the ontology. We're now going to implement the methods needed to fill out these 4 attributes.

### Getting the ontology URI

If we're dealing with an OWL ontology, it may be the case that the URI we have just used to retrieve the ontology file is not the 'official' URI of the ontology. In fact OWL provides a construct that can be used to 'state' which is the base URI of an ontology (essentially, this is equivalent to stating that an RDF resource has rdf:type http://www.w3.org/2002/07/owl#Ontology). So in the following method first we check if an URI of rdf:type OWL:Ontology exists, and return that if available (when we return None, the URI value defaults to the URI originally provided when creating the OntoInspector object - see the constructor code above):

```
def get_OntologyURI(self, return_as_string=True):
    """ 
    In [15]: [x for x in o.rdfGraph.triples((None, RDF.type, OWL.Ontology))]
    Out[15]: 
    [(rdflib.URIRef('http://purl.com/net/sails'),
      rdflib.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type'),
      rdflib.URIRef('http://www.w3.org/2002/07/owl#Ontology'))]

    Mind that this will work only for OWL ontologies.
    In other cases we just return None, and use the URI passed at loading time
    """

    test = [x for x, y, z in self.rdfGraph.triples((None, RDF.type, OWL.Ontology))]

    if test:
        if return_as_string:
            return str(test[0])
        else:
            return test[0]
    else:
        return None
```

### Extracting all the classes

Essentially, there are only **two ways to define a class**: you can either specify that an entity has a property RDF:type with value rdfs:Class, or that it has a property RDF:type with value owl:Class. Note that the owl:Class predicate is defined as a _subclass_ of rdfs:Class. The rationale for having a separate OWL class construct lies in the restrictions on OWL DL (and thus also on OWL Lite), which imply that not all RDFS classes are legal OWL DL classes. In OWL Full these restrictions do not exist and therefore owl:Class and rdfs:Class are equivalent in OWL Full (more info here: [http://www.w3.org/TR/owl-ref/](http://www.w3.org/TR/owl-ref/), section 3.1).

Thus, In order to retrieve all the classes defined in an ontology we can just query the RDF graph for triples that have this form:

someURI - rdf:type - rdf:Class OR owl:Class .

This approach will work in the majority of cases. However, things are complicated by the fact that people are sometimes sloppy when they define ontologies, or because they use different tools that automatically generate different styles of RDF code. For example, often an entity is defined as being an rdfs:subclassOf another entity, without explicitly declaring that both of them are (rdfs, or owl) classes; another common case is that one of classes mentioned in the domain/range values of properties (via the rdfs.domain and rdfs.range properties) but not declared explicitly.

Since we want to be as comprehensive as possible when looking for \*all\* the classes present in an ontology, I added a couple of methods that deal with these borderline cases. If you don't want to include all of this stuff, you can still bypass these extra checks by using the _classPredicate_ argument.

```
def __getAllClasses(self, classPredicate = "", removeBlankNodes = True):
    """  
    Extracts all the classes from a model
    We use the RDFS and OWL predicate by default; also, we extract non explicitly declared classes
    """

    rdfGraph = self.rdfGraph
    exit = []       

    if not classPredicate:          
        for s, v, o in rdfGraph.triples((None, RDF.type , OWL.Class)): 
            exit.append(s)
        for s, v, o in rdfGraph.triples((None, RDF.type , RDFS.Class)):
            exit.append(s)

        # this extra routine makes sure we include classes not declared explicitly
        # eg when importing another onto and subclassing one of its classes...
        for s, v, o in rdfGraph.triples((None, RDFS.subClassOf , None)):
            if s not in exit:
                exit.append(s)
            if o not in exit:
                exit.append(o)

        # this extra routine includes classes found only in rdfs:domain and rdfs:range definitions
        for s, v, o in rdfGraph.triples((None, RDFS.domain , None)):
            if o not in exit:
                exit.append(o)
        for s, v, o in rdfGraph.triples((None, RDFS.range , None)):
            if o not in exit:
                exit.append(o)

    else:
        if classPredicate == "rdfs" or classPredicate == "rdf":
            for s, v, o in rdfGraph.triples((None, RDF.type , RDFS.Class)):
                exit.append(s)
        elif classPredicate == "owl":
            for s, v, o in rdfGraph.triples((None, RDF.type , OWL.Class)): 
                exit.append(s)
        else:
            raise exceptions.Error("ClassPredicate must be either rdf, rdfs or owl")

    exit = remove_duplicates(exit)

    if removeBlankNodes:
        exit = [x for x in exit if not self.__isBlankNode(x)]

    return sort_uri_list_by_name(exit)
```

You probably noticed that there are a couple of other methods mentioned in the snippet above: they are used for checking if a URI is a BlankNode (which we're normally not interested in, when dealing with ontologies) and for other utility functions, such as sorting and removing duplicates from our list of classes. You'll find all the details about this stuff in the source code obviously..

Next, we want to be able to **move around the ontology hierarchy**. So we need methods to get _super_ and _sub_ classes from a given class. This is easily done by querying the graph for triples containing the rdfs.subClassOf predicate:

```
# methods for getting ancestores and descendants of classes: by default, we do not include blank nodes

def get_classDirectSupers(self, aClass, excludeBnodes = True):
    returnlist = []
    for s, v, o in self.rdfGraph.triples((aClass, RDFS.subClassOf , None)):
        if excludeBnodes:
            if not self.__isBlankNode(o):
                returnlist.append(o)
        else:
            returnlist.append(o)

    return sort_uri_list_by_name(remove_duplicates(returnlist)) 


def get_classDirectSubs(self, aClass, excludeBnodes = True):
    returnlist = []
    for s, v, o in self.rdfGraph.triples((None, RDFS.subClassOf , aClass)):
        if excludeBnodes:
            if not self.__isBlankNode(s):
                returnlist.append(s)

        else:
            returnlist.append(s)

    return sort_uri_list_by_name(remove_duplicates(returnlist))


def get_classAllSubs(self, aClass, returnlist = [], excludeBnodes = True):
    for sub in self.get_classDirectSubs(aClass, excludeBnodes):
        returnlist.append(sub)
        self.get_classAllSubs(sub, returnlist, excludeBnodes)
    return sort_uri_list_by_name(remove_duplicates(returnlist))



def get_classAllSupers(self, aClass, returnlist = [], excludeBnodes = True ):
    for ssuper in self.get_classDirectSupers(aClass, excludeBnodes):
        returnlist.append(ssuper)
        self.get_classAllSupers(ssuper, returnlist, excludeBnodes)
    return sort_uri_list_by_name(remove_duplicates(returnlist))



def get_classSiblings(self, aClass, excludeBnodes = True):
    returnlist = []
    for father in self.get_classDirectSupers(aClass, excludeBnodes):
        for child in self.get_classDirectSubs(father, excludeBnodes):
            if child != aClass:
                returnlist.append(child)

    return sort_uri_list_by_name(remove_duplicates(returnlist))
```

### Getting the top layer

We're now all set for retrieving the classes at the top of the taxonomic hierarchy of our ontology, that is, its 'top-layer'. This can be done by reusing the get\_classDirectSupers method previously defined, so to search for all classes that have no superclasses:

```
def __getTopclasses(self, classPredicate = ''):

    """ Finds the topclass in an ontology (works also when we have more than on superclass)
    """

    returnlist = []

    # gets all the classes
    for eachclass in self.__getAllClasses(classPredicate):
        x = self.get_classDirectSupers(eachclass)
        if not x:
            returnlist.append(eachclass)

    return sort_uri_list_by_name(returnlist)
```

### Reconstructing the ontology tree

Now that we know which are the top classes in our taxonomy, we can parse the tree recursively using the get\_classDirectSubs method defined above, and reconstruct the whole taxonomical structure of the ontology.

```
def __getTree(self, father=None, out=None):

    """ Reconstructs the taxonomical tree of an ontology, from the 'topClasses' (= classes with no supers, see below)
        Returns a dictionary in which each class is a key, and its direct subs are the values.
        The top classes have key = 0

        Eg.
        {'0' : [class1, class2], class1: [class1-2, class1-3], class2: [class2-1, class2-2]}
    """

    if not father:
        out = {}
        topclasses = self.toplayer
        out[0] = topclasses

        for top in topclasses:
            children = self.get_classDirectSubs(top)
            out[top] = children
            for potentialfather in children:
                self.__getTree(potentialfather, out)

        return out

    else:
        children = self.get_classDirectSubs(father)
        out[father] = children
        for ch in children:
            self.__getTree(ch, out)
```

That's it really. Given this abstract tree representation, it can be printed out differently depending on the context (html, command line) but the core will remain intact.

### Wrapping up

The [source code on GitHub](https://github.com/lambdamusic/ontosPy) contains also other utilities I added, eg for handling class comments, namespaces, for nice-printing of classes' names, and for outputting the ontology tree as an image, using the [Graphviz](http://www.graphviz.org/) library (which needs to be installed separately).

Here's an example of how OntoInspector can be used in the python interactive shell for inspecting the [Friend Of A Friend](http://xmlns.com/foaf/spec/) lightweight ontology:

```
In [1]: from onto_inspector import *

In [2]: onto = OntoInspector("http://xmlns.com/foaf/spec/20100809.rdf")         

In [3]: onto.toplayer

Out[3]: 
[rdflib.URIRef('http://xmlns.com/foaf/0.1/Agent'),
 rdflib.URIRef('http://www.w3.org/2000/01/rdf-schema#Class'),
 rdflib.URIRef('http://www.w3.org/2004/02/skos/core#Concept'),
 rdflib.URIRef('http://xmlns.com/foaf/0.1/Document'),
 rdflib.URIRef('http://xmlns.com/foaf/0.1/LabelProperty'),
 rdflib.URIRef('http://www.w3.org/2000/01/rdf-schema#Literal'),
 rdflib.URIRef('http://www.w3.org/2000/10/swap/pim/contact#Person'),
 rdflib.URIRef('http://xmlns.com/foaf/0.1/Project'),
 rdflib.URIRef('http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing'),
 rdflib.URIRef('http://www.w3.org/2002/07/owl#Thing')]

In [4]: onto.printTree()
foaf:Agent
----foaf:Group
----foaf:Organization
----foaf:Person
rdfs:Class
http://www.w3.org/2004/02/skos/core#Concept
foaf:Document
----foaf:Image
----foaf:PersonalProfileDocument
foaf:LabelProperty
rdfs:Literal
http://www.w3.org/2000/10/swap/pim/contact#Person
----foaf:Person
foaf:Project
http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing
----foaf:Person
owl:Thing
----foaf:OnlineAccount
--------foaf:OnlineChatAccount
--------foaf:OnlineEcommerceAccount
--------foaf:OnlineGamingAccount

In [5]: document = onto.find_class_byname("document")

In [6]: document
Out[6]: 
[rdflib.URIRef('http://xmlns.com/foaf/0.1/Document'),
 rdflib.URIRef('http://xmlns.com/foaf/0.1/PersonalProfileDocument')]

In [7]: document = document[0]

In [8]: document
Out[8]: rdflib.URIRef('http://xmlns.com/foaf/0.1/Document')

In [9]: onto.get_classAllSubs(document)
Out[9]: 
[rdflib.URIRef('http://xmlns.com/foaf/0.1/Image'),
 rdflib.URIRef('http://xmlns.com/foaf/0.1/PersonalProfileDocument')]

In [10]: onto.get_classAllSupers(document)
Out[10]: []

In [11]: onto.get_classComment(document)
Out[11]: rdflib.Literal('A document.', language=None, datatype=None)
```

Any comments? As I said I'm still learning/improving this... so any feedback is welcome!
