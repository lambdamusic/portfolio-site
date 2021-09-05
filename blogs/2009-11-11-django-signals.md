---
title: "Django signals"
date: "2009-11-11"
categories: 
  - "techlife"
tags: 
  - "django"
  - "signals"
---

This is a really cool feature of django that I've never explored, so I though I'd made a post about it so to remind myself of using it more often! It's discussed extensively in the docs [here](http://docs.djangoproject.com/en/dev/topics/signals/#topics-signals) and [here](http://docs.djangoproject.com/en/dev/ref/signals/#ref-signals). In a nutshell:

> Django includes a “signal dispatcher” which **helps allow decoupled applications get notified when actions occur elsewhere in the framework**. In a nutshell, signals allow certain senders to notify a set of receivers that some action has taken place. They’re especially useful when many pieces of code may be interested in the same events.
> 
> Django provides a set of built-in signals that let user code get notified by Django itself of certain actions. These include some useful notifications: **django.db.models.signals.pre\_save** & **django.db.models.signals.post\_save** Sent before or after a model’s save() method is called. **django.db.models.signals.pre\_delete** & **django.db.models.signals.post\_delete** Sent before or after a model’s delete() method is called. **django.core.signals.request\_started** & **django.core.signals.request\_finished** Sent when Django starts or finishes an HTTP request.

#### How to use them?

Really simple: modify the code below as needed and put it at the **bottom** of your models.py file (it could be located anywhere, but by putting it there we make sure it's loaded at the right time):

from django.db.models.signals import post\_save

def my\_handler(sender, instance, created, \*\*kwargs):
    if created:
        \# if the instance is effectively saved
        try:
            if instance.my\_favourite\_method():
                instance.special\_field \= instance.my\_favourite\_method()
        except:
            instance.special\_field \= "undefined"
        instance.save()

post\_save.connect(my\_handler, sender\=SomeModel)

Imagine that each time an instance of SomeModel gets saved you want to perform some other operation, such as adding something to one of its fields. **Three simple steps**: **import** the _post\_save_ signal, **define** a function _my\_handler_ that does the operation, **connect** your handler to a specific model.
