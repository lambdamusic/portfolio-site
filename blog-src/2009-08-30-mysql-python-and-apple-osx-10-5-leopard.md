---
title: "MySQL-Python and Apple OSX 10.5 (Leopard)"
date: "2009-08-30"
categories: 
  - "techlife"
  - "tips-and-tricks"
tags: 
  - "django"
  - "leopard"
  - "mysql"
  - "mysqldb"
  - "python"
---

UPDATE 30/12/09 : Snow Leopard and most recent versions of MySQL-python have broken the recipe below: you'd better check [this blog post](http://birdhouse.org/blog/2009/02/21/python-mysql-connections-on-mac-os/comment-page-1/) for an updated version (it worked for me). In a nutshell, the new method involves using the Macports installation if you're on Leopard, or specifying your 64-bit architecture during the compile process if you're on Snow Leopard... but if you're still getting errors, there's nothing else to do than [invoking the almighty google](http://www.google.com/search?hl=en&rls=en&q=install+MySQLdb+python&aq=f&aqi=g4&oq=) for help . .

\>>>

Hey there - just a quick sunday post (oh god what a nerd I am) to report on my latest experience **installing the usual stack for python/django web development** on my MacBookPro: **MySQL** \[handy links: [install info](http://dev.mysql.com/doc/refman/5.0/en/mac-os-x-installation.html) | [download page](http://dev.mysql.com/downloads/mysql/5.1.html#downloads) | [do I need the 64 bit mac package?](http://www.stata.com/support/faqs/win/64bit.html)\], the **python bindings** to MySQL ([MySQL-Python](http://sourceforge.net/projects/mysql-python/files/)) and **[Django](http://www.djangoproject.com/download/)**. Apache is not needed for now as I'll be using the django builtin server for development (and it should be already installed on your mac). Well anyways, there's lots of posts on how to install the whole thing, I tried a couple of times in the past but **always got stuck with a bloody MySQLdb error** \[_EnvironmentError: mysql\_config not found_\]. So I always resorted to the **ready-made-stack solutions** - which, by the way, work fantastically - I'm talking here about things such as [Bitnami's DjangoStack](http://bitnami.org/stack/djangostack).

\>>>

However, this time I decided to crack the problem. I installed [MySQL](http://dev.mysql.com/doc/refman/5.0/en/mac-os-x-installation.html), then downloaded the [MySQLdb package](http://sourceforge.net/projects/mysql-python/files/) manually (you can try install it using _easy-install_, but it **wont work** cause you gotta edit a couple of things first). Then followed the clear and useful instructions outlined on [this blog post by Ken Ingle](http://www.keningle.com/?p=11) (another useful post is also [this one](http://www.djangrrl.com/view/installing-django-with-mysql-on-mac-os-x/)). Summing them up:

After unpacking the files, in the _MySQL-python-1.2.2_ directory **edit** the _\_mysql.c_ file and do the following:

1) **Remove** these lines \[34 +\]:

#ifndef uint
#define uint unsigned int
#endif

2) **Change** the following \[484 +\]

uint port \= MYSQL\_PORT;
uint client\_flag \= 0;

with this:

unsigned int port \= MYSQL\_PORT;
unsigned int client\_flag \= 0;

3) Then in order to avoid the irritating **_EnvironmentError: mysql\_config not found_** just **edit** the _setup\_posix.py_ file and change the _mysql\_config.path_ into this \[line 27\]:

mysql\_config.path \= "/usr/local/mysql/bin/mysql\_config"

4) **Create** a symlink:

$ sudo ln \-s /usr/local/mysql/lib /usr/local/mysql/lib/mysql

5) **Build** and **install** (and don't let the warnings scare you)

$ sudo python setup.py build
$ sudo python setup.py install

6) Test

\>\>\> import MySQLdb
\>\>\> MySQLdb.apilevel
'2.0'

7) Enjoy (here's the [user-guide](http://mysql-python.sourceforge.net/MySQLdb.html) and an [example](http://www.wellho.net/resources/ex.php4?item=y115/sql1a.py)) ):

import MySQLdb

conn \= MySQLdb.connect(host\="localhost", user\="root", passwd\="nobodyknow", db\="amit")
cursor \= conn.cursor()

stmt \= "SELECT \* FROM overflows"
cursor.execute(stmt)

\# Fetch and output
result \= cursor.fetchall()
print result

\# get the number of rows
numrows \= int(cursor.rowcount)

\# Close connection
conn.close()
