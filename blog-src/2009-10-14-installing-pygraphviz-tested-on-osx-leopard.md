---
title: "Installing PyGraphviz [tested on OSx Leopard]"
date: "2009-10-14"
categories: 
  - "techlife"
  - "tips-and-tricks"
tags: 
  - "graphics"
  - "pygraph"
  - "python"
---

PyGraphviz is a Python interface to the Graphviz graph layout and visualization package. With PyGraphviz you can create, edit, read, write, and draw graphs using Python to access the Graphviz graph data structure and layout algorithms.

\[I was doing this in order to benefit from some of the [django-command-extension](http://code.google.com/p/django-command-extensions/wiki/GraphModels) functionalities\]

1\. Get graphviz [here](http://www.graphviz.org/) and install it (should be straightforward)

2\. [Download PyGraphViz](http://networkx.lanl.gov/pygraphviz/index.html). Make sure you download the source package. It's possible to install it through [easy\_install](http://www.michelepasin.org/blog/2009/01/27/python-easyinstall-the-peak-developers-center/) but it would throw the following error:

bash\-3.2$ easy\_install pygraphviz
Searching for pygraphviz
Reading http://pypi.python.org/simple/pygraphviz/
Reading http://networkx.lanl.gov/pygraphviz
Reading http://networkx.lanl.gov/wiki/download
Reading http://sourceforge.net/project/showfiles.php?group\_id=122233&amp;package\_id=161979
Reading http://networkx.lanl.gov/download
Best match: pygraphviz 0.99.1
Downloading http://pypi.python.org/packages/source/p/pygraphviz/pygraphviz-0........
Processing pygraphviz\-0.99.1.zip
Running pygraphviz\-0.99.1/setup.py \-q bdist\_egg \-\-dist\-dir /var/folders/Cm/C.........
Trying pkg\-config
/bin/sh: pkg\-config: command not found
/bin/sh: pkg\-config: command not found
Trying dotneato\-config
Failed to find dotneato\-config

Your graphviz installation could not be found.

Either the graphviz package is missing on incomplete
(binary packages graphviz\-dev or graphviz\-devel missing?).

If you think your installation is correct you will need to manually
change the include\_path and library\_path variables in setup.py to
point to the correct locations of your graphviz installation.

The current setting of library\_path and include\_path is:
library\_path\=None
include\_path\=None

error: None

3\. Change _setup.py_ by specifying where your graphViz installation is \[[more info here](http://groups.google.com/group/networkx-discuss/browse_thread/thread/a06ea83e37d1ff2b?pli=1)\]:

\# library\_path=None
library\_path\='/usr/local/lib/graphviz'
\# include\_path=None
include\_path\='/usr/local/include/graphviz'

4\. Install:

bash\-3.2$ python setup.py install
library\_path\=/usr/local/lib/graphviz
include\_path\=/usr/local/include/graphviz
running install
running build
running build\_py
creating build/lib.macosx\-10.4\-i386\-2.5
creating build/lib.macosx\-10.4\-i386\-2.5/pygraphviz
copying pygraphviz/\_\_init\_\_.py \-\> build/lib.macosx\-10.4\-i386\-2.5/pygraphviz
copying pygraphviz/agraph.py \-\> build/lib.macosx\-10.4\-i386\-2.5/pygraphviz
\[...... etc. etc.......\]

5\. Enjoy!:

\>\>\> import pygraphviz as pgv
\>\>\> G\=pgv.AGraph()
\>\>\> G.add\_node('a')
\>\>\> G.add\_edge('b','c')
\>\>\> G
strict graph {
        a;
        b \-\- c;
}

#To load a dot file use

\>\>\> G\=pgv.AGraph("file.dot")
