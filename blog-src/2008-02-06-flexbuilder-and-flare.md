---
title: "FlexBuilder and Flare"
date: "2008-02-06"
categories: 
  - "techlife"
tags: 
  - "flare"
  - "flash"
  - "flex"
---

Got a headache by trying to use the flash version of [Prefuse](http://prefuse.org/), which is called [Flare](http://flare.prefuse.org/), in the Flex2 builder environment (which I found out, you [can get for free if you're a student](http://www.flexregistration.com/)). Basically the [tutorial](http://flare.prefuse.org/doc/tutorial/) works fine till you reach the most interesting point: adding the Flare libraries into the project.

The library import facility doesnt seem to work: I get funny errors related to the eclipse editor that doesnt even let me visualize the file contents of the imported libraries:

> Unable to create this part due to an internal error. Reason for the failure: Editor could not be initialized.
> 
> java.lang.NullPointerException ....bla, bla bla....

So, after some googling I found out that somebody else had the same problem:

> [There's a pretty good tutorial that I, as a beginner, found straightforward. I ran into some problems when I was trying to "import a library into another project," but per Jeffrey's suggestion, I upgraded to Adobe Flex 3 beta (currently a free download). That cured my problems. Adobe Flex is apparently still a little rough around the edges. Oh right, and the tutorial provides instructions on how to develop with Flare in the Flex Builder environment.](http://flowingdata.com/2007/10/30/use-flare-visualization-toolkit-to-build-interactive-viz-for-the-web/)

Mind that the [Jeffrey](http://jheer.org/) he's talking about is the creator of Flare. [Flex 3 is the solution](http://labs.adobe.com/wiki/index.php/Flex_3)...  
So, word of advice: if you want Flex for the Flare capabilities, **don't go through release 2!!!**
