---
title: "An introduction to Neo4j"
date: "2013-04-10"
categories: 
  - "informationarchitecture"
tags: 
  - "database"
  - "graph"
  - "neo4j"
---

[Neo4j](http://www.neo4j.org/) is a recent graph-database that is rapidly accumulating success stories, especially in areas such as "_social applications, recommendation engines, fraud detection, resource authorization, network & data center management and much more_". Here's an interesting introductory lecture about by Ian Robinson at [JavaZone 2013](http://jz13.java.no/).

> Tip: [Databasetube](http://www.databasetube.com/tag/neo4j/) offers various other interesting articles about neo4j

<iframe src="http://player.vimeo.com/video/49377272" width="400" height="300" frameborder="0" webkitallowfullscreen mozallowfullscreen="" allowfullscreen=""></iframe>

A few notes from the presentation:

Premises: 
	- Data today is more connected than ever before
	- Complexity = f(size, semi-structure, connectedness)
	- Graphs are the best abstractions we have to model connectedness

The data model in neo4j: "property graph model"
	- nodes have properties (eg key-value pairs)
	- relationships have a direction, and can have properties too (eg weighted associations)

Neo4j server has a built in UI (web-based)

When to consider using a graph database:
	- lots of join tables \[connectedness\]
	- lots of sparse tables \[semi-structure\]

Neo4j fully supports ACID transactions
	- durable, consistent data
	- uses a try/success syntax

Performance
	- millions of 'joins' per second \[connections are pre-calculated at insert time!\]
	- consistent query times as dataset grows

Cypher query language
	- syntax mirrors the graphic representation of a graph 
	- one dimensional, left-to-right
	

> For a comparison of various graph databases (including Neo4j) check out this [tutorial from the ESWC'13 conference](http://www.labf.usb.ve/TUTORIAL2013/ESWC2013Tutorial/Home_files/SlidesTutorialGraphDatabases_MAC.pdf)
