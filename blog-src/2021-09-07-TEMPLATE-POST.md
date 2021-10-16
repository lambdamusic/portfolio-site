---
title: "A template post used for cloning posts"
date: "2021-09-08"
review: true
---

A few tips on making posts below.

# Adding an Image

With hyperlink to big size

[![title](/media/static/blog_img/img.jpg)](/media/static/blog_img/img.jpg)


# Obsidian workflow 

1. Open obsidian

2. Select the Vault with the blog entries in it

3. Add / Modify / Delete

4. Run `./tools/blogs-reindex` 

5. Run `./tools/site-dump-and-publish`




# Command line workflow to add a new post

## 1 Making a new post

```bash
$ new_blog_post
```
Duplicates 2021-09-07-TEMPLATE-POST.md and lets you edit it. 

Alternatively, open up Obsidian and do it from there.

## 2 Reindex the site

Once it's done, reindex the blog metadata on the site (Django DB)


```bash
$ ./tools/blogs-reindex
# syncs local MD folder with DB // add, update, delete records as needed 
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


