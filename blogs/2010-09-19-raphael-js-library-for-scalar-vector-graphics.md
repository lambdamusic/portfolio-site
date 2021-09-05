---
title: "Raphael: js library for Scalar Vector Graphics"
date: "2010-09-19"
categories: 
  - "techlife"
tags: 
  - "design"
  - "graphics"
  - "javascript"
  - "svg"
---

I don't do much (web) front-end design usually, although often I find it vital to visualize my ideas using some sort of basic but functional UI-kit. Well, if you're like me, you'll probably be happy to know about [Raphael](http://raphaeljs.com/). This is a **javascript library that sits on top of the SVG specifications** and provides a set of (very straighforward) **APIs for creating vector graphics and animations** in most browsers.

> [Scalable Vector Graphics](http://en.wikipedia.org/wiki/Scalable_Vector_Graphics) (SVG) is a family of specifications of an **XML-based file format** for describing two-dimensional vector graphics, both static and dynamic (i.e. interactive or animated). The SVG specification is an open standard that has been under development by the [World Wide Web Consortium](http://www.w3.org/Graphics/SVG/) (W3C) since 1999. SVG images and their behaviors are defined in XML text files. This means that they can be searched, indexed, scripted and, if required, compressed. Since they are XML files, SVG images can be created and edited with any text editor, but specialized SVG-based drawing programs are also available.

Writing SVG stuff can be very painful, but using Raphael it almost becomes fun. The official site gives you various examples (eg check out the slick [polar clock](http://raphaeljs.com/polar-clock.html), or the [diagram elements](http://raphaeljs.com/graffle.html)), and code that shows how easy it is to get started:

[![Screen shot 2010-09-19 at 23.15.05.png](/media/static/blog_img/Screen-shot-2010-09-19-at-23.15.05.png)](http://www.michelepasin.org/blog/wp-content/uploads/2010/09/Screen-shot-2010-09-19-at-23.15.05.png)

Looking forward to spend more time on this. For now, I've just collected a few good learning resources about it, which I thought I'd share:

- The official [homepage](http://raphaeljs.com/), which contains various examples and all the [documentation](http://raphaeljs.com/reference.html)
- [An Introduction to the Raphael JS Library](http://net.tutsplus.com/tutorials/javascript-ajax/an-introduction-to-the-raphael-js-library/): a nice blog post that shows how to build a little mood meter from the ground up
- Another [blog post](http://dev.opera.com/articles/view/raphael-a-javascript-api-for-svg/) showing how to create a typical "progress throbber", as seen in Apple interfaces, with a few lines of code
- [Raphael Live](http://craic.com/tutorials/javascript/raphael_live/raphael_live.html#): a simulator of the js library, for testing your code easily within a browser's window
- Lots of categorized raphael examples at [www.irunmywebsite.com](http://www.irunmywebsite.com/raphael/additionalhelp.php?)
- An interesting discussion about the advantages of [Raphael vs jQuery SVG](http://stackoverflow.com/questions/588718/jquery-svg-vs-raphael) (also, make sure you check out all the [questions tagged 'raphael' at stackoverflow](http://stackoverflow.com/questions/tagged/raphael))

Below, some screenshots of a fancy [clock](http://raphaeljs.com/polar-clock.html), a [tiger](http://raphaeljs.com/tiger.html), and a [graph](http://raphaeljs.com/analytics.html), all built entirely via Raphael.

[![Screen shot 2010-09-19 at 23.30.43.png](/media/static/blog_img/Screen-shot-2010-09-19-at-23.30.43.png)](http://www.michelepasin.org/blog/wp-content/uploads/2010/09/Screen-shot-2010-09-19-at-23.30.43.png)

[![Screen shot 2010-09-19 at 23.34.19.png](/media/static/blog_img/Screen-shot-2010-09-19-at-23.34.19.png)](http://www.michelepasin.org/blog/wp-content/uploads/2010/09/Screen-shot-2010-09-19-at-23.34.19.png)

[![Screen shot 2010-09-19 at 23.34.32.png](/media/static/blog_img/Screen-shot-2010-09-19-at-23.34.32.png)](http://www.michelepasin.org/blog/wp-content/uploads/2010/09/Screen-shot-2010-09-19-at-23.34.32.png)

..
