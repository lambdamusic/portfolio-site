---
title: "AJAX in Lisp with JQuery"
date: "2008-02-27"
categories: 
  - "techlife"
tags: 
  - "jquery"
  - "lisp"
  - "web"
---

I was asked to give an example of lisp+ajax, so once I prepared it I thought it could be of help to other people too :-)

First of all, I am not a professional lisper at all, just got to know it a little during the last two years. The code I'm presenting here might not be the best one, but it works and essentially shows you how to do cool ajax stuff by using lisp \[btw, some of this code comes from somebody who knows about lisp much more than I do, [this guy here](http://www.kmi.open.ac.uk/people/dave/)\].

Anyways, let's get going: we want to create a very very simple webapp that changes the color of some text in the page, using an ajax call. So we'll have **one main page**, another **page which gives back the code for updating the main page** through ajax, and a **couple of js files** we want to use for the front-end functionality (among them, the fantastic [jquery](http://jquery.com/)).

First of all, we'll need two handy packages for setting up a fully-working lisp server: [hunchentoot](http://www.weitz.de/hunchentoot/) and [cl-who](http://weitz.de/cl-who/) (the more you learn about these packages, the better it is - and go through the examples - they're really useful!). Once you've installed them, using [asdf-install](http://www.cliki.net/ASDF-Install) or whatever-you-like, let's load them up and set a couple of environment variables.

(asdf:operate 'asdf:load-op :hunchentoot)
(asdf:operate 'asdf:load-op :cl-who)

(use-package :cl-who)
(setq hunchentoot:\*catch-errors-p\* nil
hunchentoot:\*log-lisp-backtraces-p\* t)

Then we define a couple of functions for starting/stopping the server and setting up the dispatcher table, which is where the mapping between web-pages in the application and lisp functions in the backend is specified. We'll have three of these mappings: one for the **main** page, one for the page that serves the ajax changes (**what-color?**), and one for passing the static files, such as js and css (**static/**).

(defvar \*web-server\* nil)

(defun start-server ()
(setq hunchentoot:\*dispatch-table\*
(nconc
(mapcar (lambda (args)
(apply #'hunchentoot:create-prefix-dispatcher args))
'(("/static/" serve-static)
("/what-color" what-color?)
("/main" main)))
(list #'hunchentoot:default-dispatcher)))
(setf \*web-server\* (hunchentoot:start-server :port 3000)))

(defun stop-server ()
(hunchentoot:stop-server \*web-server\*))

When the start-server function is called, it'll load the dispatch table and start the sever on port 3000.

The hardest thing to do now, before creating the functions that output the web-pages, is to set up the functions that handle the static files. First of all define your **location**, so that lisp knows where the root folder of the webapp is. That's how it looks on my mac - you probably want to change that according to needs.

(defvar \*location\* "/Users/myname/dev-try/hunchentoot-examples/")

Then the function for serving the static files (**serve-static**). In this example web-app we'll only have two of them (see below), but you might want to have more (e.g. css, jpg etc..). The other three functions below basically retrieve the static file, check its mime-type and pass it back to the dispatcher.

(defun serve-static ()
(let\* ((uri (hunchentoot:request-uri))
(file (subseq uri (length "/static/"))))
(format \*error-output\* "serve-static: file=~S~%" file)
(http-write-file file (mime-types file))))

(defun http-write-file (filename mime-type)
"Send contents of FILENAME to the HTTP stream, along with its MIME-TYPE."
(setf (hunchentoot:content-type) mime-type)
(let\* ((stream (hunchentoot:send-headers))
(buffer (make-array 1024 :element-type '(unsigned-byte 8 )))
(local-filename (format nil "~astatic/~a" \*location\* filename)))
(with-open-file (in local-filename :element-type '(unsigned-byte 8 ))
(loop for pos = (read-sequence buffer in)
until (zerop pos)
do (write-sequence buffer stream :end pos)))))

(defun mime-types (filename)
(let ((ext (subseq filename (+ 1 (position #. filename :from-end t)))))
(second (assoc ext '(("txt" "text/plain")
("css" "text/css")
("lisp" "text/plain")
("html" "text/html")
("js" "text/javascript")
("png" "image/png"))
:test #'string=))))

(defun write-http-stream (mime-type payload)
(setf (hunchentoot:content-type) mime-type)
(write-sequence payload (hunchentoot:send-headers)))

That was the trickiest part. Now let's just create the functions that produce the html code to be passed to the browser/javascript. Before that, just a couple of useful macros that wrap the standard cl-who functions. **With-html** for creating html code without a header, and **with-html-top** for creating also the header.

(defmacro with-html (&body body)
\`(with-html-output-to-string
(\*standard-output\* nil :prologue nil :indent nil)
(htm ,@body)))

(defmacro with-html-top (&body body)
\`(with-html-output-to-string
(\*standard-output\* nil :prologue t :indent nil)
,@body))

Finally, the pages we can call from the browser. **Main** creates the main page of the app, linking to the javascript files. **what-color?** just outputs a random color name out of a predefined list:

(defun main ()
(with-html-top
(:html (:head
(:title "Home page")
(:script :type "text/javascript" :src "/static/jquery.pack.js")
(:script :type "text/javascript" :src "/static/my\_functions.js"))
(:body
(:p :id "text" "Hi there - this is the only page for now")
(:a :href "javascript:changeColor()" "click here to change the color!")))))

(defun what-color? ()
(let ((color-list '("blue" "red" "lavender" "black" "yellow"
"orange" "mandarin" "MistyRose" "Olive")))
(nth (random (length color-list)) color-list)))

That's it really, for the backend. Now all you have to do is to create a **folder called 'static'** wherever you specified the \*location\* variable to point at. Inside the folder, put a copy of [the latest JQuery code](http://docs.jquery.com/Downloading_jQuery) (**jquery.pack.js**), and create a new file called **my\_functions.js** with this elementary function (sorry - that's all the ajax we're getting for now...) . It's a simple function that calls the server for getting a color name, and uses it to change the color of a dom element.

function changeColor() {
$.get("what-color",
function(data){
$("#text").css("color",data);
}
);
}

Almost done. Enter **(start-server)** in the lisp listener, and go to **http://localhost:3000/main** to see your first lisp-ajax application! \[if the colors don't show properly, make sure you are using Firefox\]

Have fun!
