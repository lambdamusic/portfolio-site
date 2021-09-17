---
title: "Preloading stuff in django's interactive shell"
date: "2010-11-17"
categories: 
  - "techlife"
  - "tips-and-tricks"
tags: 
  - "django"
  - "shell"
---

[Django's shell](http://docs.djangoproject.com/en/dev/ref/django-admin/#shell) is a fantastic way to interact with all the components of your django application, eg when testing new functionalities or debugging a nasty error. Sometimes though you end up loading the same variables or importing the same modules every time you run the shell , for example because you are trying out a large function that needs being refined through a trial and error process.

Opening up the shell and reloading all the components you need to have handy can thus become a bit tedious; here's an easy way to go around this problem. In doing this, I've just been inspired some code found in the handy [django-extensions](https://github.com/django-extensions/django-extensions) app. The extensions ship with a number of [command modules](http://code.google.com/p/django-command-extensions/wiki/CommandExtensions), that is, functions that you can run from the unix shell using the usual _python manage.py some\_command_ syntax.

The module I'm talking about here is called **shell\_plus** - it's an enhanced version of the Django shell. It will autoload all your models making it easy to work with the ORM right away. Here's the implementation:

\# django\_extensions/management/commands/shell\_plus.py  
  
import os  
from django.core.management.base import NoArgsCommand  
from optparse import make\_option  
  
class Command(NoArgsCommand):  
    option\_list = NoArgsCommand.option\_list + (  
        make\_option('--plain', action='store\_true', dest='plain',  
            help\='Tells Django to use plain Python, not IPython.'),  
        make\_option('--no-pythonrc', action='store\_true', dest='no\_pythonrc',  
            help\='Tells Django to use plain Python, not IPython.'),  
    )  
    help = "Like the 'shell' command but autoloads the models of all installed Django apps."  
  
    requires\_model\_validation = True  
  
    def handle\_noargs(self, \*\*options):  
        \# XXX: (Temporary) workaround for ticket #1796: force early loading of all  
        \# models from installed apps. (this is fixed by now, but leaving it here  
        \# for people using 0.96 or older trunk (pre \[5919\]) versions.  
        from django.db.models.loading import get\_models, get\_apps  
        loaded\_models = get\_models()  
  
        use\_plain = options.get('plain', False)  
        use\_pythonrc = not options.get('no\_pythonrc', True)  
  
        \# Set up a dictionary to serve as the environment for the shell, so  
        \# that tab completion works on objects that are imported at runtime.  
        \# See ticket 5082. 
        from django.conf import settings  
        imported\_objects = {'settings': settings}  
        for app\_mod in get\_apps():  
            app\_models = get\_models(app\_mod)  
            if not app\_models:  
                continue  
            model\_labels = ", ".join(\[model.\_\_name\_\_ for model in app\_models\])  
            print self.style.SQL\_COLTYPE("From '%s' autoload: %s" % (app\_mod.\_\_name\_\_.split('.')\[\-2\], model\_labels))  
            for model in app\_models:  
                try:  
                    imported\_objects\[model.\_\_name\_\_\] = getattr(\_\_import\_\_(app\_mod.\_\_name\_\_, {}, {}, model.\_\_name\_\_), model.\_\_name\_\_)  
                except AttributeError, e:  
                    print self.style.ERROR\_OUTPUT("Failed to import '%s' from '%s' reason: %s" % (model.\_\_name\_\_, app\_mod.\_\_name\_\_.split('.')\[\-2\], str(e)))  
                    continue  
        try:  
            if use\_plain:  
                \# Don't bother loading IPython, because the user wants plain Python.  
                raise ImportError  
            import IPython  
            \# Explicitly pass an empty list as arguments, because otherwise IPython  
            \# would use sys.argv from this script.  
            shell = IPython.Shell.IPShell(argv=\[\], user\_ns=imported\_objects)  
            shell.mainloop()  
        except ImportError:  
            \# Using normal Python shell  
            import code  
            try: \# Try activating rlcompleter, because it's handy.  
                import readline  
            except ImportError:  
                pass  
            else:  
                \# We don't have to wrap the following import in a 'try', because  
                \# we already know 'readline' was imported successfully.  
                import rlcompleter  
                readline.set\_completer(rlcompleter.Completer(imported\_objects).complete)  
                readline.parse\_and\_bind("tab:complete")  
  
            \# We want to honor both $PYTHONSTARTUP and .pythonrc.py, so follow system  
            \# conventions and get $PYTHONSTARTUP first then import user.  
            if use\_pythonrc:  
                pythonrc = os.environ.get("PYTHONSTARTUP")  
                if pythonrc and os.path.isfile(pythonrc):  
                    try:  
                        execfile(pythonrc)  
                    except NameError:  
                        pass  
                \# This will import .pythonrc.py as a side-effect  
                import user  
            code.interact(local=imported\_objects)

Essentially, this is what's going on here:

a. A **subclass of NoArgsCommand is created** following the standard approach stated in Django's [docs for creating custom management commands](http://docs.djangoproject.com/en/dev/howto/custom-management-commands/) .

b. All the **applications** in your django project and the related **models** get **loaded**, and their references are added to the **imported\_objects** dictionary, eg when the code reads:

```

imported_objects = {'settings': settings}
```

c. The code tries to **load the best python shell** available: iPython if present, otherwise the normal python shell with the necessary libraries are called.

...

That's all. The key line to look at is therefore the last one, that is:

```

# .......
code.interact(local=imported_objects)
```

That's what launches the interpreter and initializes it with the _**imported\_objects**_ dictionary; this dictionary contains all the (extra) symbols that we want to make available through the new python interpreter instance. So in order to have more stuff there all we have to do is add more elements to that dictionary, eg:

```

# .......
alist = range(1000)
imported_objects['alist'] = alist
code.interact(local=imported_objects)
```

Insert these two lines right before the last line of the script above, save it using a new name (eg. _my\_fancyshell.py_ )in the _/management/commands/_ directory of one of your applications (it needs to be there so that django interprets it as a custom command), and the game is done. Now you can invoke

```

bash-3.2$ python manage.py my_fancyshell.py
```

from the unix command line, and the 'alist' symbol will be available. Obviously in a real world situation you might end up loading and adding to the _imported\_objects_ dictionary various many things too, but the principle will remain the same!

...
