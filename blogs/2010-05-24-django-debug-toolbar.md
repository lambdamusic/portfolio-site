---
title: "Django debug toolbar"
date: "2010-05-24"
categories: 
  - "techlife"
tags: 
  - "debug"
  - "django"
---

[Django Debug Toolbar 0.8](http://vimeo.com/6640136) from [Idan Gazit](http://vimeo.com/idangazit) on [Vimeo](http://vimeo.com).

This is just an amazingly useful application you might want to add to your django development tools.

Installation is a breeze:

```

$ easy_install django-debug-toolbar
```

...

Then you need to add some parameters to your _settings.py_, as explained [here](http://github.com/robhudson/django-debug-toolbar/blob/master/README.rst). It's likely that you don't want the debug-toolbar to show on your production site as well, but only where you're doing development. So a more portable alternative to the usual way to add the debug-toolbar parameters is the following:

```

# set to True if you're on the production server
LIVESERVER = False

# ..... other settings....

if not LIVESERVER:
	# stuff for the debug toolbar
	INSTALLED_APPS += 	('debug_toolbar',)
	INTERNAL_IPS = ('127.0.0.1',)
	MIDDLEWARE_CLASSES += ( 'debug_toolbar.middleware.DebugToolbarMiddleware', )

```

...

The _LIVESERVER_ variable is the only thing you've got to manually change when copying your code to the production server...
