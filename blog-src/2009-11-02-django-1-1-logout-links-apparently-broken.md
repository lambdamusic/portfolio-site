---
title: "Django 1.1: LogOut links apparently broken"
date: "2009-11-02"
categories: 
  - "techlife"
tags: 
  - "django"
---

I lost quite a few hours on this, but the solution was simple. The other day I realized that all the **Log-in / Log-out hyperlinks in the admin were messing things up** in various ways.

Either by inserting a mysterious 'None' string in the url, or by adding the necessary url terminations (_/logout, /login_) to the wrong place (e.g. _/admin/application\_name/logout_ instead of _/admin/logout_). Tried to google this a bit, [found some results](http://www.mail-archive.com/django-updates@googlegroups.com/msg33118.html) but nothing was apparently related..

Basically what happened is that when upgrading to [Django 1.1](http://www.djangoproject.com/weblog/2009/jul/29/1-point-1/). I didn't update also the base.html file in my templates/admin ... small thing really, but as I said it did manage to give me a headache. So, advice is, **when upgrading make sure to update all the admin templates you're making use of (e.g. for customizing them)!**. Follows an example of how the upgrade has changed things in base.html..

\# in admin/base.html

\# used to be:
<a href\="{{ root\_path }}logout/"\>{% trans 'Log out' %}</a\>

\# instead now is:
{% url admin:logout as logout\_url %}
