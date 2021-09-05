---
title: "Setting up Django Registration"
date: "2011-01-14"
categories: 
  - "techlife"
  - "tips-and-tricks"
tags: 
  - "django"
  - "email"
  - "python"
  - "registration"
  - "smtp"
  - "smtpd"
---

Django's [admin framework](https://docs.djangoproject.com/en/1.4/ref/contrib/admin/) includes the basic functionalities for logging in and out of the admin site, but if you're building a so-called 'social' application and want people to be able to sign-up, log in and thus benefit from additional site functionalities then you need to use a more generic 'registration' application. The good news is: most of the work has already been done, so it's just a matter of putting things together correctly.

I found a nicely written [blog post](http://www.stonemind.net/blog/2007/04/13/django-registration-for-newbies/) on this topic, so in what follows I'm just doing a re-cap of the main steps involved and adding some other useful info.

Before we start: what follows has been tested on Django 1.1 Django 1.3, Python 2.6 and MySQL (note: on 13/8/12 I revised this post so that the code would work on django 1.3 - many thanks to the folks who left comments and pointed out what needed to be updated!)

### 1) Install

Download the package from [bitbucket](https://bitbucket.org/ubernostrum/django-registration/downloads) and add it to your application directory (or put it somewhere else and then modify your python path as needed). Then add the 'registration' app to the _installed\_apps_ tuple in your settings.py:

INSTALLED\_APPS \= (
    'django.contrib.auth',
    'django.contrib.humanize',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    \# etc..
    'registration',
)

### 2) Syncdb

Do a quick _[syncdb](http://docs.djangoproject.com/en/dev/ref/django-admin/#syncdb)_ from the console, which will result in one new table being created in the DB, 'RegistrationProfile'. All it contains is its primary key, the 'user' key, and the 'activation code' fields. Now we've got the data structures needed for setting up the registration application!

\> python manage.py syncdb

### 3) Setting.py

Create some registration **settings** in settings.py:

ACCOUNT\_ACTIVATION\_DAYS\=7
EMAIL\_HOST\='localhost'
EMAIL\_PORT\=1023
EMAIL\_HOST\_USER\='username'
EMAIL\_HOST\_PASSWORD\='password'

Obviously you've got to **change** the settings above depending on your specific server setup (more information is available [here](https://bitbucket.org/ubernostrum/django-registration/src/tip/docs/quickstart.rst) or [here](http://docs.djangoproject.com/en/dev/ref/settings/?from=olddocs#email-host)). Also, see point 7 below if you're just testing things out without a SMTP server available.

### 4) Urls.py

Include the required registration **urls** to your urls.py:

urlpatterns \= patterns(",
  (r'^admin/', include('django.contrib.admin.urls')),
  (r'^accounts/', include('registration.urls')),
)

### 5) Templates

Add the registration **templates** to your django-templates directory. The django-registration package we downloaded earlier on doesn't include any templates, but you can easily find _some_ of them online (for example [here](http://code.djangoproject.com/browser/djangoproject.com/django_website/templates/registration)). Anyways, no need to do that: I took those templates and added some other ones too so to create the minimal working package that'll get you going (that doesn't include any fancy css styling but all the basic html stuff is there). You can [download the templates here](https://www.box.com/s/68191c48af306e450c29), expand the zip file and put it in templates/registration.

### 6) Done! Let's recap..

We're now **ready** to go. Let's pause for a moment and recap what we achieved: we installed and activated django-registration, which sets up a whole bunch of new urls. These are divided into two groups:

**a)** _/login_, _/logout_, the two-step password change at _password/change/_ and _password/change/done/_; the four-step password reset at _password/reset/_, _password/reset/confirm/_, _password/reset/complete/_ and _password/reset/done/_. This is the original URL specification source code (you can see it on [bitbucket](https://bitbucket.org/ubernostrum/django-registration/src/d36a38202ee3/registration/auth_urls.py) too) :

\# from django-registration / registration / auth\_urls.py
urlpatterns \= patterns('',
                       url(r'^login/$',
                           auth\_views.login,
                           {'template\_name': 'registration/login.html'},
                           name\='auth\_login'),
                       url(r'^logout/$',
                           auth\_views.logout,
                           {'template\_name': 'registration/logout.html'},
                           name\='auth\_logout'),
                       url(r'^password/change/$',
                           auth\_views.password\_change,
                            {'template\_name': 'registration/password\_change\_form.html'},
                           name\='auth\_password\_change'),
                       url(r'^password/change/done/$',
                           auth\_views.password\_change\_done,
                            {'template\_name': 'registration/password\_change\_done.html'},
                           name\='auth\_password\_change\_done'),
                       url(r'^password/reset/$',
                           auth\_views.password\_reset,
                            {'template\_name': 'registration/password\_reset\_form.html'},
                           name\='auth\_password\_reset'),
                       url(r'^password/reset/confirm/(?P<uidb36>\[0-9A-Za-z\]+)-(?P<token>.+)/$',
                           auth\_views.password\_reset\_confirm,
                            {'template\_name': 'registration/password\_reset\_confirm.html'},
                           name\='auth\_password\_reset\_confirm'),
                       url(r'^password/reset/complete/$',
                           auth\_views.password\_reset\_complete,
                            {'template\_name': 'registration/password\_reset\_complete.html'},
                           name\='auth\_password\_reset\_complete'),
                       url(r'^password/reset/done/$',
                           auth\_views.password\_reset\_done,
                            {'template\_name': 'registration/password\_reset\_done.html'},
                           name\='auth\_password\_reset\_done'),
)

**b)** the second group of urls are _/activate_ and _/register_: This is the original URL specification source (see it on [bitbucket](https://bitbucket.org/ubernostrum/django-registration/src/d36a38202ee3/registration/backends/default/urls.py)) :

\# django-registration / registration / backends / default / urls.py 
urlpatterns \= patterns('',
                       url(r'^activate/complete/$',
                           direct\_to\_template,
                           { 'template': 'registration/activation\_complete.html' },
                           name\='registration\_activation\_complete'),
                       \# Activation keys get matched by w+ instead of the more specific
                       \# \[a-fA-F0-9\]{40} because a bad activation key should still get to the view;
                       \# that way it can return a sensible "invalid key" message instead of a
                       \# confusing 404.
                       url(r'^activate/(?P<activation\_key>w+)/$',
                           activate,
                           { 'backend': 'registration.backends.default.DefaultBackend' },
                           name\='registration\_activate'),
                       url(r'^register/$',
                           register,
                           { 'backend': 'registration.backends.default.DefaultBackend' },
                           name\='registration\_register'),
                       url(r'^register/complete/$',
                           direct\_to\_template,
                           { 'template': 'registration/registration\_complete.html' },
                           name\='registration\_complete'),
                       url(r'^register/closed/$',  \# UNUSED
                           direct\_to\_template,
                           { 'template': 'registration/registration\_closed.html' },
                           name\='registration\_disallowed'),
                        \# this is the default django login module 
                       (r'', include('registration.auth\_urls')),
                       )

### 7) Testing

If you're testing things on a development server you might not have access to an [SMTP server](http://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol) (needed to test the email-based registration process). In such a case you can still try out your application using a workaround. In your settings.py file change the registration settings with the following ones:

EMAIL\_HOST \= 'localhost'
EMAIL\_PORT \= 1025
EMAIL\_HOST\_USER \= "
EMAIL\_HOST\_PASSWORD \= "
EMAIL\_USE\_TLS \= False
DEFAULT\_FROM\_EMAIL \= 'testing@example.com'

Then open up another **console window** and run a temporary 'dummy' SMTP server with [python](http://docs.python.org/library/smtpd.html):

bash\-3.2$ python \-m smtpd \-n \-c DebuggingServer localhost:1025

This local SMTP server remains there waiting for incoming messages. If now you go to _/accounts/register/_, fill out the form and hit ‘send’ you’ll see the registration email printed out in the console. Basically what happened is this: the ‘dummy’ python SMTP server we’ve just set up picked up django’s email-sending request and consequently printed out the email contents. If this is indeed what happened, it means that your code is working properly… and that you can use the url provided in the email to test the **activation** functionality too.

For example, here is what you would see in the console after registering:

```

---------- MESSAGE FOLLOWS ----------
Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: quoted-printable
Subject: Activate your djangoproject.com account - you have 2 days!
From: testing@example.com
To: michele.pasin@hotmail.com
Date: Wed, 12 Jan 2011 16:49:59 -0000
Message-ID: <20110112164959.3366.35638@mymac.local>
X-Peer: 127.0.0.1


Someone, hopefully you, signed up for a new account at djangoproject.com using this email address. If it was you, and you'd like to activate and use your
account, click the link below or copy and paste it into your web browser's address bar:

http://127.0.0.1:8000/accounts/activate/6342fca5ffd430a820be6d98acde6e59a4c2d29c/

If you didn't request this, you don't need to do anything; you won't receive any more email from us, and the account will expire automatically in two days.

------------ END MESSAGE ------------
```

**Pasting** the 'activation' url in your browser should allow you to complete the registration process and check the rest of your code.

Finally, keep in mind also that the django-registration application sends out emails that contain your site’s URL for the activation link, and that URL is dynamically determined using the ['sites' application](https://docs.djangoproject.com/en/dev/ref/contrib/sites/?from=olddocs/) (normally added via settings.py). By default, your domain name is listed as ‘example.com’, and the easiest way to change this is to log into the admin application and click on the ‘Sites’ link on the admin home page to get to the relevant entry.

\===== ++ =====

#### Some other possibly useful links:

Fromt the Django website:- [User authentication in django](http://docs.djangoproject.com/en/1.1/topics/auth/)
- [Sending emails](http://docs.djangoproject.com/en/dev/topics/email/)
From the Django book:- [Chapter 12: Sessions, users, and registration](http://www.djangobook.com/en/beta/chapter12/)
