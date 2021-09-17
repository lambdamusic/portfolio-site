---
title: "Using jquery's autocomplete in django admin: how about inlines?"
date: "2009-09-30"
categories: 
  - "techlife"
  - "tips-and-tricks"
tags: 
  - "admin"
  - "autocomplete"
  - "django"
---

I still haven't solved this problem entirely, and I'll tell you why. Well the issue has been addressed by many, and among them probably the first and most influential solution is Jannis Leidel's ['An autocomplete form widget for ForeignKey model fields'](http://jannisleidel.com/2008/11/autocomplete-form-widget-foreignkey-model-fields/).

Leidel says:

> \[..\] my question is, if this could be done on a more abstract level for enhancing relations. when having a foreignkey, you get the browse-icon (lens) right near the input-field. it´d be awesome to search the relations just by typing something into the field … the autocomplete-functionality should then search the related entries on the basis of the defined search-fields.

Here's a nice **screencast** of the the result \[UPDATE: unfortunately the screencast is not available anymore\]:

[![Picture 1](/media/static/blog_img/picture-11.png "Picture 1")](http://www.flickr.com/photos/jannis/3028766217/)

**Leidel's solution is not a copy&paste type of thing**, however it's very useful to study his code so to understand what's going on there, and then replicate it in your specific user-scenario. That's exactly what several people have done.

Nonetheless, **reusing is more agile that doing things from scratch**, isn't it? So, after a bit of research I reached the conclusion that the most interesting and reusable (meaning, plug-and-play) django implementations of jquery's autocomplete are two:

1. the [_admin extensions_ section of the django-extensions project](http://code.google.com/p/django-command-extensions/wiki/AdminExtensions) on google code

**PROs**: it extends django's raw\_input widget, so while you can make use of the autocomplete you can still click on the lens and select the object you want from a new objects-list window (see screencast below). Also, you can enter the id of the object and the autocomplete will fill in straightaway the human-readable form of it (not sure how useful it is, but I like it) **CONs**: supports only one-2-many relationships, that is, it doesn't work with many2many or inlines5. another project on google code called - surprise - [django-autocomplete](http://code.google.com/p/django-autocomplete/) !

**PROs**: very compact (just one file, no new apps to include). Works with one2many AND many2many **CONs**: again, no support for inlines...

After having a go with both of them I decided to use the first one \[the admin extensions section of the [django-extensions project](http://code.google.com/p/django-command-extensions/wiki/AdminExtensions)\], cause I don't need many2many support and I really liked the fact that the standard 'raw-id' behaviour is still available. Here's a nice screencast (by the way I just realized that this one has been made by Jannis Leidel too, so I guess it's sort of an evolution of the previous one) \[UPDATE #2: also this screencast is not available anymore! what's going on with mr Leidel?\]:

[![Picture 3](/media/static/blog_img/picture-31.png "Picture 3")](http://www.flickr.com/photos/jannis/3246408003/)

Conclusion: there's only one BIG problem - **it doesn't work with [inlines](http://docs.djangoproject.com/en/dev/ref/contrib/admin/#inlinemodeladmin-objects)** out-of-the-box ! I'm looking at extending it now... will keep you posted!
