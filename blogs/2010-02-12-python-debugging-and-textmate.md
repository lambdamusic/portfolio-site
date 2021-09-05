---
title: "Python debugging and Textmate"
date: "2010-02-12"
categories: 
  - "techlife"
  - "tips-and-tricks"
tags: 
  - "debug"
  - "pdb"
  - "python"
  - "textmate"
---

I've never realized that among the [many things Textmate does well](http://manual.macromates.com/en/) there's also python debugging. Well, to be precise Textmate doesn't do much as it just relies on **python's default debugger, called [PDB](http://docs.python.org/library/pdb.html)**. Ok, probably PDB isn't the cutting edge debugger you're looking for, but it's worth a try imho.

Nothing to install in order to try: just open up a python script with textmate, hit **cmd+shift+D** and a debug-terminal window will open. The **essential commands for Pdb** are (the first letter is the one to digit):

- s(tep): Execute the current line, stop at the first possible occasion (either in a function that is called or on the next line in the current function).
- r(eturn): Continue execution until the current subroutine returns.
- n(ext): Continue execution until the next line in the current function is reached or it returns.
- p(rint) expression: Evaluate the expression in the current context and print its value.
- a(rgs): Print the argument list of the current function.
- q(uit): Quit from the debugger
- c(ont(inue)): Instead of quitting, Continue execution, only stop when a breakpoint is encountered.

A nice and clear crash course of Pbd can also be found [here](http://pythonconquerstheuniverse.wordpress.com/category/the-python-debugger/).

[![](http://www.michelepasin.org/blog/wp-content/uploads/2010/02/picture-12.png?w=300 "Picture 1")](http://www.michelepasin.org/blog/wp-content/uploads/2010/02/picture-12.png)

...

OTHER TEXTMATE TIPS AND TRICKS:

- [PdbTextMateSupport](http://pypi.python.org/pypi/PdbTextMateSupport/0.3) is a plugin that gives you a more powerful debugger within Textmate: a [detailed description of its (simple) installation is here.](http://www.libertypages.com/clarktech/?p=192)
- a nice post about [10 cool TextMate tips](http://domhay.com/blog/2009/10-cool-textmate-tips): most of them are HTML/CSS related, but worth checking out!
- Textmate basic [tutorial](http://projects.serenity.de/textmate/tutorials/basics/). This is a must for everyone who wants to use TextMate seriously (available also in Japanese!)
- [Three plugins](http://al3x.net/2008/12/03/how-i-use-textmate.html) that'll make textmate shine even more: **Project Plus** (adds extra functionalities to the project drawer), **GetBundles** (a better version of the old GetBundle), **Ack In Project** (a much faster 'search in project' function).
- Nice [screencast](http://screencasts.textmate.org/math_and_column_selections.mov) on how to use the **Math** bundle

...
