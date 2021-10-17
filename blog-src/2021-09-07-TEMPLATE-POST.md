---
title: "A TEMPLATE POST USED FOR CLONING POSTS"
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

5. Test on http://127.0.0.1:8000/words/?type=review

6. Run `./tools/site-dump-and-publish`


# KEY FACTS 

1. Blog files need to start with a date with hyphens eg `2021-09-08`
2. Each blog entry should contain a title and a date. Optionally, also a review flag.
3. The webapp uses the DB registry as an index, and the local files for the MD contents. 
4. The ID of blog entries is the file name. Blog ID is stored in the `md_file` field of Publications. Internal DB ID is the auto-increment number as usual.
5. Blogs permalink is similar to the Wordpress one, eg "/2018/11/23/exploring-scholarly-publications-via-dbpedia/". Permalink depends entirely on file name (blog ID), not the publication date metadata found in MD file.
6. Posts in 'review' mode are still visible in local Django. Eg http://127.0.0.1:8000/blog/2021/09/07/TEMPLATE-POST/




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

OR 

Test on http://127.0.0.1:8000/words/?type=review


## 4 Publish it

```bash
$ site-dump-and-publish
```

If Django is running, the wget extraction script will pull the entire site, copy it to /docs and push it to Github


