---
title: "Using Django-MPTT: lessons learned..."
date: "2009-09-15"
categories: 
  - "techlife"
tags: 
  - "django"
  - "mptt"
  - "tree"
---

Here we are again with Django and [MPTT](http://code.google.com/p/django-mptt/) 0.3 (I already have [other posts about it](http://www.michelepasin.org/blog/?p=275)). After working with it for a bit I realized that **things were breaking mysteriously**, and only recently understood why that happened, so I thought I'd share this pearl of wisdom. Essentially this has to do with the way tree-elements must be created if you want the usual tree-navigation methods (e.g. _get\_descendants_ or _get\_ancestors_) to work as expected.

Suppose your Django model looks like this:

from django.db import models  
  
import mptt  
  
class PossessionNew(models.Model):  
    possname = models.CharField(max\_length=50, unique=True)  
    parent = models.ForeignKey('self', null=True, blank=True, related\_name='children')  
  
mptt.register(PossessionNew,)

Suppose now that you want to **start instantiating the PossessionNew model** (sorry about the name, it's just taken out the context of the application I was working on).

In my case I was creating the tree from other data which needed some pre-processing in order to determine the hierarchical information, so I thought I'd **create first all the instances, and then 'link' them by setting their _.parent_ attribute as needed**. This turned out to be the **wrong way of doing it**. In other words, what I did was this: first, creating the instances, and second, create the relationships. E.g.:

bash-3.2$ ./runshell.my  
Python 2.5.1 (r251:54863, Sep 11 2008, 14:17:35)  
\[GCC 4.0.1 (Apple Computer, Inc. build 5250)\] on darwin  
Type "help", "copyright", "credits" or "license" for more information.  
(InteractiveConsole)  
\>>> from poms.pomsapp.models import \*  
\>>> p1 = PossessionNew(possname="test11")  
\>>> p2 = PossessionNew(possname="test22")  
\>>> p3 = PossessionNew(possname="test33")  
\>>> p1.save()  
\>>> p2.save()  
\>>> p3.save()  
\>>> p3.parent = p2  
\>>> p2.parent = p1  
\>>> p3.save()  
\>>> p2.save()

Everything seemed to work fine and it also looked fine on the admin interface. However, **things didn't work when trying to use MPTT APIs**. For example, after restarting the shell:

\>>> p2 = PossessionNew.objects.get(possname="test22")  
\>>> p2.get\_children()  
\[\]  \# weird!  
\>>> p2.get\_  
p2.get\_ancestors               p2.get\_descendants             p2.get\_next\_sibling            p2.get\_previous\_sibling  
p2.get\_children                p2.get\_next\_by\_created\_at      p2.get\_previous\_by\_created\_at  p2.get\_root  
p2.get\_descendant\_count        p2.get\_next\_by\_updated\_at      p2.get\_previous\_by\_updated\_at  p2.get\_siblings  
\>>> p2.parent  
<PossessionNew: test11\>  
\>>> p2.children.all()  
\[<PossessionNew: test33\>\]  
\>>> p2.get\_ancestors()  
\[<PossessionNew: test11\>\]  
\>>> p2.get\_descendants()  
\[\] \# weird!

As you can see, we have some erratic behavior here, in fact the _get\_descendants_ and other similar methods don't produce the desired output..

I soon realized that the error lies in the fact that when creating children manually - e.g. by setting the _.parent_ attribute of an instance - the other fields needed for MPTT to manage the tree are not updated.

So, here's the **right way of doing this**. When operating with the tree you must **always use the _insert\_at_ and _move\_to_ methods** that come with the MPTT library. So, for example:

\>>> p3 = PossessionNew(possname = "test333")  
\>>> p1 = PossessionNew(possname = "test111")  
\>>> p2 = PossessionNew(possname = "test222")  
\>>> p1.save()  
\>>> p2.save()  
\>>> p3.save()  
\>>> p2.move\_to(p1)  
\>>> p3.move\_to(p2)

\[**Update 17/11/10:**\] almost by chance, I finally understood what the problem was here.. [mptt has a problem with updating instances already stored in memory](http://groups.google.com/group/django-mptt-dev/browse_thread/thread/b2c68adde7f4fb92). What follows is still valid, but there are other ways around the problem too eg. [check this link too](http://code.google.com/p/django-mptt/issues/detail?id=17).

Now let's check again whether the model inheritance works all right (I usually have to **restart the shell** in order to check this, otherwise the modifications are not loaded properly. I haven't figured out yet why this happens...):

\>>> p2 = PossessionNew.objects.get(possname = "test222")  
\>>> p2.get\_descendants()  
\[<PossessionNew: test333\>\]  
\>>> p2.get\_ancestors()  
\[<PossessionNew: test111\>\]

Now it all makes more sense, doesn't it? Notice that in this case we used the _**move\_to**_ method. We could also have used _**insert\_at**_ (check the [docs](http://django-mptt.github.com/django-mptt/)). Remember also that we've been using these methods with instances up to now (=**instance methods**). If necessary, you could also achieve the same results by means of the TreeManager custom manager (=**custom manager methods**). So, for example:

\>>> p1 = PossessionNew(possname = "test11")  
\>>> PossessionNew.tree.insert\_node(p1, None, commit=True)  
<PossessionNew: test11\>  
\>>> p2 = PossessionNew(possname = "test22")  
\>>> PossessionNew.tree.insert\_node(p2, p1, commit=True)  
<PossessionNew: test22\>  
\>>> p3 = PossessionNew(possname = "test33")  
\>>> PossessionNew.tree.insert\_node(p3, p2, commit=True)  
<PossessionNew: test33\>

That's it. Follows a list of the model instance methods [MPTT makes available](http://django-mptt.github.com/django-mptt/models.html#mpttmodel-instance-methods):

> **get\_ancestors(ascending=False)** -- creates a QuerySet containing the ancestors of the model instance. These default to being in descending order (root ancestor first, immediate parent last); passing True for the ascending argument will reverse the ordering (immediate parent first, root ancestor last).
> 
> **get\_children()** -- creates a QuerySet containing the immediate children of the model instance, in tree order. The benefit of using this method over the reverse relation provided by the ORM to the instance's children is that a database query can be avoided in the case where the instance is a leaf node (it has no children).
> 
> **get\_descendants(include\_self=False)** -- creates a QuerySet containing descendants of the model instance, in tree order. If include\_self is True, the QuerySet will also include the model instance itself.
> 
> **get\_descendant\_count()** -- returns the number of descendants the model instance has, based on its left and right tree node edge indicators. As such, this does not incur any database access.
> 
> **get\_next\_sibling()** -- returns the model instance's next sibling in the tree, or None if it doesn't have a next sibling.
> 
> **get\_previous\_sibling()** -- returns the model instance's previous sibling in the tree, or None if it doesn't have a previous sibling.
> 
> **get\_root()** -- returns the root node of the model instance's tree.
> 
> **get\_siblings(include\_self=False)** -- creates a QuerySet containing siblings of the model instance. Root nodes are considered to be siblings of other root nodes. If include\_self is True, the QuerySet will also include the model instance itself.
> 
> **insert\_at(target, position='first-child', commit=False)** -- positions the model instance (which must not yet have been inserted into the database) in the tree based on target and position (when appropriate). If commit is True, the model instance's save() method will be called before the instance is returned.
> 
> **is\_child\_node()** -- returns True if the model instance is a child node, False otherwise.
> 
> **is\_leaf\_node()** -- returns True if the model instance is a leaf node (it has no children), False otherwise.
> 
> **is\_root\_node()** -- returns True if the model instance is a root node, False otherwise.
> 
> **move\_to(target, position='first-child')** -- moves the model instance elsewhere in the tree based on target and position (when appropriate).
