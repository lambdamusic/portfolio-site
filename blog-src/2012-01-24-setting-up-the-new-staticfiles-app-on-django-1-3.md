---
title: "Setting up the new 'staticfiles' app on Django 1.3"
date: "2012-01-24"
categories: 
  - "techlife"
  - "tips-and-tricks"
tags: 
  - "django"
  - "static"
---

Even if I've been using Django 1.3 for a while now, I've been holding off on some of it new features, such as the new way to handle static files via a [new app](https://docs.djangoproject.com/en/dev/howto/static-files/) called (guess what) staticfiles . Essentially, what the new static app does is allowing you to leave all static files within the /static directory of each of the django apps you're using. This is for development; when you're deploying and (most likely) want these files to be served via a (faster) separate server process, the staticfiles app helps you gather all of them into a predefined directory by using a handy shell command.

That's the gist of it. I finally took a look at django.contrib.staticfiles last week, so here's a brief report on how to get it to work (p.s. a couple of related threads on stack overflow can be found [here](http://stackoverflow.com/questions/7620307/how-do-i-serve-css-to-django-in-development) and [here](http://stackoverflow.com/questions/4565935/django-staticfiles-app-help)).

### 1\. Set up the static and media paths settings

My previous settings looked like this:

\# the site root is one level up from where settings.py is
SITE\_ROOT = os.path.dirname(os.path.realpath(\_\_file\_\_)).rsplit('/', 1)\[0\]
MEDIA\_ROOT = os.path.join(SITE\_ROOT, 'static')
MEDIA\_URL = '/static/'
ADMIN\_MEDIA\_PREFIX = '/static/adminmedia1.3/'

The media root contained all of my static files, some of which I had to copy in there manually, each time I added a new django app to my project. On the production server, the MEDIA\_URL is mapped to a local path (in the apache conf settings) that is essentially a duplicate of the /static directory we have in the development server. The only difference, the static stuff is delivered directly by Apache, bypassing django (=so to make it faster).

The **new way** of declaring these variables is this instead:

MEDIA\_URL = '/media/uploads/'
STATIC\_URL = '/media/static/'
ADMIN\_MEDIA\_PREFIX = '/media/static/admin/'

\# Absolute path to the directory that holds media uploaded
\# I keep the uploads folder at the project-root level server
MEDIA\_ROOT = os.path.join(SITE\_ROOT, 'uploads') 

\# physical location of extra static files in development server
STATICFILES\_DIRS = (
    os.path.join(SITE\_ROOT, 'myproject/static'),
)
\# path used with "python manage.py collectstatic"
\# I normally put this at the project-root level that contains also the wsgi files for apache
STATIC\_ROOT = os.path.join(SITE\_ROOT, 'apache/static')

Obviously on a production server, you will have to set up the required aliases in the [apache conf](https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/modwsgi/#serving-files) file, so that MEDIA\_URL and STATIC\_URL are pointing at the right physical locations:

Alias /media/uploads/ /path/to/mysite.com/uploads/
Alias /media/static/ /path/to/mysite.com/apache/static/

The [django docs](https://docs.djangoproject.com/en/dev/howto/static-files/) explain the new approach with these words:

> In previous versions of Django, it was common to place static assets in MEDIA\_ROOT along with user-uploaded files, and serve them both at MEDIA\_URL. Part of the purpose of introducing the staticfiles app is to make it easier to keep static files separate from user-uploaded files.
> 
> For this reason, you need to make your MEDIA\_ROOT and MEDIA\_URL different from your STATIC\_ROOT and STATIC\_URL.
> 
> The STATIC\_ROOT directory is not necessary in the development server: in fact is only used if you call the collectstatic manangement command. It's not needed to add the directory to the STATICFILES\_DIRS setting to serve your static files!
> 
> Furthemore, the STATICFILES\_DIRS variable tells Django of the location of static files which are not within specific applications. Mind that during the 'collection' operations also these files will be copied into the STATIC\_ROOT directory.

### 2\. Add context processors and the app

Add the required context processor in setting.py:

TEMPLATE\_CONTEXT\_PROCESSORS += 'django.core.context\_processors.static'

Add also the new static app to your installed apps:

INSTALLED\_APPS = (
....    
    'django.contrib.staticfiles',    
.....
)

> Keep in mind that it's very likely that in your templates you will have to manually change all references to MEDIA\_URL into STATIC\_URL!

### 3\. Url configuration

On your **development** server, this is what you would do:

from django.contrib.staticfiles.urls import staticfiles\_urlpatterns
\# ... the rest of your URLconf goes here ...
urlpatterns += staticfiles\_urlpatterns()

This will inspect your STATIC\_URL setting and wire up the view to serve static files accordingly. Don't forget to set the STATICFILES\_DIRS setting appropriately to let django.contrib.staticfiles know where to look for files additionally to files in app directories.

> **WARNING**: the staticfiles\_urlpatterns helper function will only work if DEBUG is True and your STATIC\_URL setting is neither empty nor a full URL such as http://static.example.com/ (more info [here](https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-development-view)).

Finally, mind that in this new approach you will need to arrange for serving of files in MEDIA\_ROOT yourself; **staticfiles does not deal with user-uploaded files at all**. You can, however, use django.views.static.serve() view for serving MEDIA\_ROOT in development (for more info see [Serving other directories](https://docs.djangoproject.com/en/dev/howto/static-files/#serving-other-directories)).

if settings.LOCAL\_SERVER:     \# ===> static files on local machine    
    urlpatterns += patterns('', 
        (r'^media/uploads/(?P<path>.\*)$', 'django.views.static.serve', 
            {'document\_root': settings.MEDIA\_ROOT, 'show\_indexes': True}),
        )

In the end, I conflated the two things into this code (ps I've added a variable called LOCAL\_SERVER to quickly see which platform I'm on):

if settings.LOCAL\_SERVER:     \# ===> static files on local machine
    from django.contrib.staticfiles.urls import staticfiles\_urlpatterns
    urlpatterns += staticfiles\_urlpatterns()    
    urlpatterns += patterns('', 
        (r'^media/uploads/(?P<path>.\*)$', 'django.views.static.serve', 
            {'document\_root': settings.MEDIA\_ROOT, 'show\_indexes': True}),
        )

### 4\. On your production server

Easy: in your urlconf there's no need to do anything, as static urls are usually handled by Apache directly. However for that to happen what you have to do is collect all static files into the directory that apache is looking into, that is, the one specified with the STATIC\_ROOT setting. This is how you do it:

> `python manage.py collectstatic`

This shell command will a) look in the /static/ directory of each of the apps of yours INSTALLED\_APPS setting. b) look in directories you specify in the STATICFILES\_DIRS setting.

…and copy whatever it finds into the STATIC\_ROOT directory, as defined in your settings (ps: it'll preserve the original directory structure).

That's all folks!
