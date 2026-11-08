# README  

Personal portfolio site  http://www.michelepasin.org/


## Tech info

A Django app which is mirrored in local using `wget` and rendered as a static site in /docs.

Requires **Python 3.9** (Django 2.1.3 depends on `distutils`, removed in Python 3.12+). See `requirements.txt`.

See also:

* [A static site generator using Django, Wget and Github Pages](https://www.michelepasin.org/blog/2021/10/29/django-wget-static-site/index.html) 


## Blog posts

Posts are markdown files in Dropbox (`NVALT/005-blog/Blog`, its own git repo); the database only indexes them. After adding or editing a post, run `./tools/blogs-reindex`.

Besides `title`, `date`, `review`, `description`, `categories` and `tags`, the front matter can carry:

* `project: "<name>"` - links the post to a project (the `<name>` in `/projects/<name>/`), so it appears under that project's writing.
* `video: "<YouTube id>"` - marks the post as a piece of music, listed on the Sounds page with that video's thumbnail.

The full reference, with an example, is in the template post: `Blog/2030-09-07-TEMPLATE-POST.md` in the blog folder (a copy is in `examples/blogs-src/`).
