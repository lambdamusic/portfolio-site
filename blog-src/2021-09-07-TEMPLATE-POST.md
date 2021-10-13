---
title: "A template post that will not be made visible"
date: "2021-09-07"
review: true
---

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Adding an Image

With hyperlink to big size

[![title](/media/static/blog_img/img.jpg)](/media/static/blog_img/img.jpg)


## 1 Making a new post

```bash
$ new_blog_post
```
Duplicates 2021-09-07-TEMPLATE-POST.md and lets you edit it. 

Alternatively, open up Obsidian and do it from there.

## 2 Reindex the site

Once it's done, reindex the blog metadata on the site (Django DB)


```bash
$ blogs_reindex
# just adds newly created blogs 
$ blogs_reindex --delete
# => empty the previously registered blogs first / like a hard sync
$ blogs_reindex --all 
# => refresh metadata for all posts, even if they preexists // used for syncing edits to 'review' or other tags (NOT THE CONTENT)

```

NOTE All items, even with 'review' = True, are added to the DB
NOTE the blogs contents (= text) never enter the DB! Just the blog metadata.


## 3 Testing a new post in review

* log in Django admin
  * http://127.0.0.1:8000/admin/researchapp/publication/?review__exact=1
* use the admin link 'view on site' 


## 4 Publish it

```bash
$ site-dump-and-publish
```

If Django is running, the wget extraction script will pull the entire site, copy it to /docs and push it to Github