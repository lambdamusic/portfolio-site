---
title: "The power of django's Q objects"
date: "2010-07-20"
categories: 
  - "techlife"
tags: 
  - "django"
  - "q_objects"
  - "query"
---

I've been spending some time today doing research on how to best use django's Q objects. Then I did a bit of testing myself and decided to put this whole thing together for future's sake, you know, for the time when I'll find myself lost and in need some coding recipe.

First things first: the **official documentation**.

- Django doc: [Complex lookups with Q objects](http://docs.djangoproject.com/en/dev/topics/db/queries/#complex-lookups-with-q-objects) The main intro
- Django doc: [OR lookups](http://www.djangoproject.com/documentation/models/or_lookups/) More in-depth examples

Now... let's get started by resurrecting the simple model used in the [django Tutorial](http://docs.djangoproject.com/en/dev/intro/tutorial01/), **Polls**, and adding a few **instances** to play with:

\# ==> in models.py
from django.db import models
import datetime

class Poll(models.Model):
        question = models.CharField(max\_length=200)
        pub\_date = models.DateTimeField('date published')

\# ==> add some instances from the shell
>>> p = Poll(question='what shall I make for dinner', pub\_date=datetime.date.today())
>>> p.save()
>>> p = Poll(question='what is your favourite meal?', pub\_date=datetime.datetime(2009, 7, 19, 0, 0)) #one year ago
>>> p.save()
>>> p = Poll(question='how do you make omelettes?', pub\_date=datetime.date.today())
>>> p.save()

## What are Q Objects Handy for?

In a nutshell, the main reason why you might want to use them is because you need to do **complex queries**, for example involving OR and AND statements a the same time.

Imagine that you want to retrieve all polls whose question **contains the word 'dinner' OR 'meal'**. The usual 'filter' option lets you do the following:

\>>> Poll.objects.filter(question\_\_contains='dinner').filter(question\_\_contains='meal')
\[\]

But this is **not really what we want**, is it? We just got a **concatenation of AND** statements (= all constraints need to be satisfied), while **we wanted an OR** (=at least one of the constraints needs to be satisfied). This is where Q objects become useful:

\>>> from django.db.models import Q
\# a simple query
>>> Poll.objects.filter(Q(question\_\_contains='dinner'))
\[<Poll: what shall I make **for** dinner>\]
\# two constraints linked by AND
>>> Poll.objects.filter(Q(question\_\_contains='dinner') & Q(question\_\_contains='meal'))
\[\]
\# two constraints linked by OR - that's it!
>>> Poll.objects.filter(Q(question\_\_contains='dinner') | Q(question\_\_contains='meal'))
\[<Poll: what shall I make **for** dinner>, <Poll: what **is** your favourite meal?>\]

Note that if you don't specify any logical connector the Q sequence is implicitly interpreted as AND:

\# no logical connector is interpreted as AND
>>> Poll.objects.filter(Q(question\_\_contains='dinner'), Q(question\_\_contains='meal'))
\[\]

Things start getting more interesting when creating complex queries:

\# eg (A OR B) AND C:
>>> Poll.objects.filter((Q(question\_\_contains='dinner') | Q(question\_\_contains='meal')) & Q(pub\_date=datetime.date.today()))
\[<Poll: what shall I make **for** dinner>\]

## Dynamic Query Building

Now, it is likely that you want to build up queries like the ones above dynamically. This is another place where Q objects can save lots of time....for example, when constructing **search engines** or **faceted browsers** where the interface lets a user **accumulate search filters** in an incremental manner.

One way to handle this situation is by creating **lists of Q objects**, and then **combining them together** using python's [operator](http://docs.python.org/library/operator.html#operator.and_) and [reduce](http://docs.python.org/library/functions.html#reduce) methods:

\>>> import operator
\# create a list of Q objects
>>> mylist = \[Q(question\_\_contains='dinner'), Q(question\_\_contains='meal')\]
\# OR
>>> Poll.objects.filter(reduce(operator.or\_, mylist))
\[<Poll: what shall I make **for** dinner>, <Poll: what **is** your favourite meal?>\]
\# AND
>>> Poll.objects.filter(reduce(operator.and\_, mylist))
\[\]

Now, if you're building the query dynamically you probably won't know in advance which are the filters you have to use. It is likely instead that you find yourself having to **generate a list of Q objects programatically** from a list of strings representing queries to your models:

\# string representation of our queries
>>> predicates = \[('question\_\_contains', 'dinner'), ('question\_\_contains', 'meal')\]
\# create the list of Q objects and run the queries as above..
>>> q\_list = \[Q(x) **for** x **in** predicates\]
>>> Poll.objects.filter(reduce(operator.or\_, q\_list))
\[<Poll: what shall I make **for** dinner>, <Poll: what **is** your favourite meal?>\]
>>> Poll.objects.filter(reduce(operator.and\_, q\_list))
\[\]

\# now let's append another filter to the query-strings..
>>> predicates.append(('pub\_date', datetime.date.today()))
>>> predicates
\[('question\_\_contains', 'dinner'), ('question\_\_contains', 'meal'), ('pub\_date', datetime.date(2010, 7, 19))\]
\# .. and the results will change too
>>> q\_list = \[Q(x) **for** x **in** predicates\]
>>> Poll.objects.filter(reduce(operator.or\_, q\_list))
\[<Poll: what shall I make **for** dinner>, <Poll: what **is** your favourite meal?>, <Poll: how do you make omelettes?>\]
>>> Poll.objects.filter(reduce(operator.and\_, q\_list))
\[\]

## Query Expansion and Q Objects

Using query expansion syntax you could normally do things **like this**:

\>>> mydict = {'question\_\_contains': 'omelette', 'pub\_date' : datetime.date.today()}
>>> Poll.objects.filter(\*\*mydict)
\[<Poll: how do you make omelettes?>\]

Here you are basically **sequencing AND statements which are built dynamically** from some string values.

A really cool feature of django ORM is that you can **keep doing this** even **while using Q objects**. In other words, you can delegate all the 'normal' stuff to the query expansion mechanism, while instead resorting to Q objects whenever you need more complex queries, such an OR statement.

For example (remember to put the dictionary always in second position):

\# OR plus query expansion
>>> Poll.objects.filter(reduce(operator.or\_, q\_list), \*\*mydict)
\[<Poll: how do you make omelettes?>\]
\# AND plus query expansion
>>> Poll.objects.filter(reduce(operator.and\_, q\_list), \*\*mydict)
\[\]

In the **first** case, we have one result only because, although the OR constraint on _q\_list_ is would match more stuff by itself, _\*\*mydict_ is exploded as a series of constraints connected by AND, thus making _\[Poll: how do you make omelettes?\]_ the only matchable object. In the **second** case instead there are no results at all simply because we are asking for a Poll instance that satisfies simultaneously all the constraints (which doesn't exist)!

## Other Resources

That's all for now! As I said, I found quite a **few very good posts** about the subject online and I strongly advise you to **check them out too** in order to have a clearer picture of how Q objects work.

- [Adding Q objects in Django](http://bradmontgomery.blogspot.com/2009/06/adding-q-objects-in-django.html) Shows another method to chain Q objects together using 'add'
- [A Tip on Complex Django Queries](http://jehiah.cz/archive/django-q-objects) Discusses how queries need to be written in order to produce the expected mySQL code
- [The power of Q](http://www.djangozen.com/blog/the-power-of-q) Really nice article that overviews all the major features of Q objects (and, or, negation, picking)
- [Dynamic Django queries (or why kwargs is your friend)](http://www.nomadjourney.com/2009/04/dynamic-django-queries-with-kwargs/) Overview of dynamic querying with django
