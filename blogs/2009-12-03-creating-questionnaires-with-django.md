---
title: "Creating Questionnaires with Django"
date: "2009-12-03"
categories: 
  - "techlife"
tags: 
  - "django"
  - "questionnaire"
  - "userstudy"
---

Simple and useful application from Aperte: [Django Questionnaire](http://djangoquest.aperte-it.com/). The Django Questionnaire app allows you to easily **set up a working questionnaire**, complete with **email-invitations** and **CSV export** functionality. This app allows you to spread your questions over multiple pages (**categories**), and currently supports **4 types of answers**.

[![](http://www.michelepasin.org/blog/wp-content/uploads/2009/12/picture-1.png?w=300 "Picture 1")](http://www.michelepasin.org/blog/wp-content/uploads/2009/12/picture-1.png)

The application is pretty **simple** and **well** **designed**. Useful for doing large user-studies, for example. The download page lets you have it packaged as a django project, but transforming it into a reusable app is not too difficult (I've done that but I'm not posting it here because of several other little hacks I had to do so to accommodate the project I'm using the questionnaire for).

**Tip**: if you're using **django 1.1** one little thing that might help you get going quickly is changing these lines of _templates/admin/admin\_index.html_:

```


{% block stylesheet %}{% load adminmedia %}{% admin_media_prefix %}css/dashboard.css{% endblock %}

```

..with this:

```


{% block extrastyle %}{{ block.super }}
<link rel="stylesheet" type="text/css" href="{% load adminmedia %}
{% admin_media_prefix %}css/dashboard.css" />
{% endblock %}

```

By the way, if you don't feel like setting up the questionnaire yourself you can easily create one on [Pervidet.com](http://www.pervidet.com/), which is (I assume) managed by the guys at [Aperte](http://www.aperte-it.com/).
