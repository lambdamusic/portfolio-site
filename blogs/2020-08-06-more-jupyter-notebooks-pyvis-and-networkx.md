---
title: "More Jupyter notebooks: pyvis and networkx"
date: "2020-08-06"
categories: 
  - "data-science"
tags: 
  - "graph"
  - "jupyter"
  - "python"
  - "visualization"
---

Lately I've been spending more time creating Jupyter notebooks that demonstrate how to use the [Dimensions API for research analytics.](https://api-lab.dimensions.ai/) In this post I'll talk a little bit about two cool Python technologies I've discovered for working with graph data: pyvis and networkx.

### pyvis and networkx

The [networkx](https://networkx.github.io/documentation/stable/reference/introduction.html) and [pyvis](https://pyvis.readthedocs.io/en/latest/tutorial.html) libraries are used for _generating_ and _visualizing_ network data, respectively.

Pyvis is fundamentally a python wrapper around the popular [Javascript visJS library.](https://visjs.github.io/vis-network/examples/) 
Networkx, instead, of is a pretty sophisticated package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.


```python
>>> from pyvis.network import Network
>>> import networkx as nx
# generate generic network graph instance
>>> nx_graph = nx.Graph()
# add some nodes and edges
>>> nx_graph.nodes[1]['title'] = 'Number 1'
>>> nx_graph.nodes[1]['group'] = 1
>>> nx_graph.nodes[3]['title'] = 'I belong to a different group!'
>>> nx_graph.nodes[3]['group'] = 10
>>> nx_graph.add_node(20, size=20, title='couple', group=2)
>>> nx_graph.add_node(21, size=15, title='couple', group=2)
>>> nx_graph.add_edge(20, 21, weight=5)
>>> nx_graph.add_node(25, size=25, label='lonely', title='lonely node', group=3)
# instantiatet pyvis network
>>> nt = Network("500px", "500px")
# populates pyvis network from networkx instance
>>> nt.from_nx(nx_graph)
>>> nt.show("nx.html")
```

It took me a little to familiarise with the libraries' concepts and to generate some basic graphs. So, the tutorials linked below are meant to provide some reusable _code_ building blocks for working with these tools.

Once you get the hang of it though, the fun part begins. What are the best data variables to represent in the graph? What color coding strategy is making it easier to explore the data? How many nodes/edges to display? Can we add some interactivity to the visualizations? Check out the resulting visualizations below for more ideas.

### Dataviz: concepts co-occurence network

The [Building a concepts co-occurence network](https://api-lab.dimensions.ai/cookbooks/2-publications/Concepts-network-graph.html) notebook shows how to turn document keywords extracted from 'semantic web' publications into a simple topic map - by virtue of their co-occurrence within the same documents.

See also the standalone html version of the interactive visualization: [concepts\_network\_2020-08-05.html](http://api-sample-data.dimensions.ai/dataviz-exports/concets-cooccurence/concepts_network_2020-08-05.html)

[![graph2](/media/static/blog_img/graph2-1024x513.jpg)](http://www.michelepasin.org/blog/wp-content/uploads/2020/08/graph2.jpg)

 

### Dataviz: Organizations Collaboration Network

The [Building an Organizations Collaboration Network Diagram](https://api-lab.dimensions.ai/cookbooks/8-organizations/3-Organizations-Collaboration-Network.html) notebook shows how to use publications' authors and [GRID](https://grid.ac/) data to generate a network of collaborating research organizations.

See also the standalone html version of the interactive visualization: [network\_2\_levels\_grid.412125.1.html](http://api-sample-data.dimensions.ai/dataviz-exports/3-Organizations-Collaboration-Network/network_2_levels_grid.412125.1.html)

[![graph1](/media/static/blog_img/graph1-1024x515.jpg)](http://www.michelepasin.org/blog/wp-content/uploads/2020/08/graph1.jpg)
