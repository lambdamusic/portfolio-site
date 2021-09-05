---
title: "Yolk : Python packages index"
date: "2009-10-27"
categories: 
  - "techlife"
tags: 
  - "python"
---

> [Yolk](http://pypi.python.org/pypi/yolk) is a Python tool for obtaining information about packages installed by distutils, setuptools and easy\_install and querying packages on PyPI (Python Package Index a.k.a. The Cheese Shop).
> 
> Yolk can list all the packages installed by distutils or setuptools on your system by >=Python2.5 or packages installed by setuptools if you have <=Python2.4. You can see which packages are active, non-active or in development mode and show you which have newer versions available by querying PyPI.

**$ yolk -l** List all installed Python packages

**$ yolk -a** List only the activated packages installed (Activated packages are normal packages on sys.path you can import)

**$ yolk -n** List only the non-activated (--multi-version) packages installed

**$ yolk -l -f License,Author nose==1.0** Show the license and author for version 1.0 of the package \`nose\`

**$ yolk --entry-map nose** Show entry map for the nose package

**$ yolk --entry-points nose.plugins** Show all setuptools entry points for nose.plugins

\>>> e.g.:

```

[mac]@mac99:~>yolk -l
BzrTools        - 1.18.0       - active development (/System/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/site-packages)
Conch           - 0.8.0        - active development (/System/Library/Frameworks/Python.framework/Versions/2.5/Extras/lib/python)
Django          - 1.0.2-final  - active
Loom            - 1.4.0dev0    - active development (/System/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/site-packages)
PIL             - 1.1.6        - active
PyRSS2Gen       - 1.0.0        - active development (/System/Library/Frameworks/Python.framework/Versions/2.5/Extras/lib/python)
Python          - 2.5.1        - active development (/System/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/lib-dynload)
Twisted Lore    - 0.3.0        - active development (/System/Library/Frameworks/Python.framework/Versions/2.5/Extras/lib/python)
Twisted Mail    - 0.4.0        - active development (/System/Library/Frameworks/Python.framework/Versions/2.5/Extras/lib/python)
Twisted Names   - 0.4.0        - active development (/System/Library/Frameworks/Python.framework/Versions/2.5/Extras/lib/python)
Twisted News    - 0.3.0        - active development (/System/Library/Frameworks/Python.framework/Versions/2.5/Extras/lib/python)
Twisted Runner  - 0.2.0        - active development (/System/Library/Frameworks/Python.framework/Versions/2.5/Extras/lib/python)
Twisted Web     - 0.7.0        - active development (/System/Library/Frameworks/Python.framework/Versions/2.5/Extras/lib/python)
Twisted Words   - 0.5.0        - active development (/System/Library/Frameworks/Python.framework/Versions/2.5/Extras/lib/python)
Twisted         - 2.5.0        - active development (/System/Library/Frameworks/Python.framework/Versions/2.5/Extras/lib/python)
altgraph        - 0.6.8.dev    - active development (/System/Library/Frameworks/Python.framework/Versions/2.5/Extras/lib/python)
antlr-python-runtime - 3.0.1        - non-active

```

...
