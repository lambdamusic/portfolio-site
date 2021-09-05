---
title: "A bookmarklet for searching delicious"
date: "2010-01-05"
categories: 
  - "techlife"
tags: 
  - "bookmarklet"
  - "delicious"
  - "javascript"
  - "search"
---

This has been long overdue for me. A **way to quickly search** [**delicious.com**](http://delicious.com/) **without relying on third-party apps** (which often you have to pay for). And it's got to be super simple too: something like a bookmarklet that you click on and then takes you there. Just one of those things you never have the time to do....

So today I got around doing it. I didn't know much about [bookmarklets](http://en.wikipedia.org/wiki/Bookmarklet) but a few google searches gave me all I needed.  These are a few links I found useful while working on this little thing:- [What are bookmarklets?](http://www.mvps.org/dmcritchie/ie/bookmarklets.htm)
- [bookmarklets.com](http://www.bookmarklets.com/)
- [Various search bookmarklets you can easily reverse-engineer](https://www.squarefree.com/bookmarklets/search.html#google)
- [a perl script that makes any javascript code ready for being used as a bookmarklet](http://daringfireball.net/2007/03/javascript_bookmarklet_builder)

Essentially bookmarklets are **javascript code formatted in a browser-friendly syntax**, that is, by url-escaping all of its characters. So I set off to create a bookmarklet for opening delicious at a specific tag-page. This button will take whatever you have highlighted on the web page and search for that string on delicious **as a tag** (not as a search string! but obviously you can modify that). If you have nothing selected the script should ask the user for a value to use.

The bookmarklet would look something like the following: [search on delicious](//delicious.com/tag/" + escape(q).replace(/ /g, "+"); void 0)

Mind that t**he bookmarklet above won't work** **if you drag it to your browser button-bar**, 'cause WordPress stripped off its behaviour (for security reasons I suppose). Too bad - you can easily recreate it yourself. The source code was something like this (note that **it should be all on a single line**,):

```

<a href="javascript:q = "" + (window.getSelection ? window.getSelection() : document.getSelection ? document.getSelection() : document.selection.createRange().text); if (!q) q = prompt("You didn't select any text.  Enter a search phrase:", ""); if (q!=null) location="http://delicious.com/tag/" + escape(q).replace(/ /g, "+"); void 0"
>search on delicious</a>
```

The script above worked for me on Apple's Safari - the only other thing I had to do was url-escaping it. Thus the code would look as follows (again, make sure it is on a single line):

```

javascript:q%20=%20%22%22%20+%20(window.getSelection%20?%20window.getSelection()%20:%20document.getSelection%20?%20document.getSelection()%20:%20document.selection.createRange().text);%20if%20(!q)%20q%20=%20prompt(%22You%20didn't%20select%20any%20text.%20%20Enter%20a%20search%20phrase:%22,%20%22%22);%20if%20(q!=null)%20location=%22http://delicious.com/tag/%22%20+%20escape(q).replace(/%20/g,%20%22+%22);%20void%200
```

You can paste the code above onto a browser's url bar to test it :-).

But if you want to save it as a bookmarklet do the following: copy this code, open up the 'Show all Bookmarks' window on Safari and create a new bookmark named 'delicious search' (or anything else), right click on the newly created bookmark and hit the 'edit address' command. Finally, in the address field paste the code you have copied and you're ready to go!

[![](/media/static/blog_img/picture-2.png "Picture 2")](http://www.michelepasin.org/blog/wp-content/uploads/2010/01/picture-2.png) [![](/media/static/blog_img/picture-3.png "Picture 3")](http://www.michelepasin.org/blog/wp-content/uploads/2010/01/picture-3.png)

That's it! Last thing: you might want to **search only through your personal tags** on delicious (that's what I do most of the time). All you have to do is modify the search string by replacing the '/tag/' ending with '/username/', where 'username' is your delicious username.. that's the standard url format delicious.com accepts for searching personal tags. So:

```

javascript:q%20=%20%22%22%20+%20(window.getSelection%20?%20window.getSelection()%20:%20document.getSelection%20?%20document.getSelection()%20:%20document.selection.createRange().text);%20if%20(!q)%20q%20=%20prompt(%22You%20didn't%20select%20any%20text.%20%20Enter%20a%20search%20phrase:%22,%20%22%22);%20if%20(q!=null)%20location=%22http://delicious.com/YOUR-USERNAME/%22%20+%20escape(q).replace(/%20/g,%20%22+%22);%20void%200
```

In conclusion, using the same approach you can create bookmarklets of all sorts!

...
