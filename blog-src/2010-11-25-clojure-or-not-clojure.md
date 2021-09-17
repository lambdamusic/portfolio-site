---
title: "Clojure or not clojure?"
date: "2010-11-25"
categories: 
  - "techlife"
tags: 
  - "clojure"
  - "dynamic"
  - "functional"
  - "java"
  - "language"
  - "lisp"
---

[Clojure](http://clojure.org/) is a quite recent programming language that's becoming popular among developers; the big selling point is that it's [functional](http://clojure.org/state) and [dynamically](http://en.wikipedia.org/wiki/Dynamic_typing#Dynamic_typing) typed (such as Lisp or Python), but since it uses Java's Virtual Runtime as its platform it also accommodates the needs of the many developers have been growing up in the Java world.

The book [Programming Clojure](http://www.pragprog.com/titles/shcloj/programming-clojure) sums up well the pros of this language:

> Clojure is **elegant**. Clojure’s clean, careful design lets you write programs that get right to the essence of a problem, without a lot of clutter and ceremony. Clojure is **Lisp reloaded**. Clojure has the power inherent in Lisp, but is not constrained by the history of Lisp. Clojure is a **functional** language. Data structures are immutable, and functions tend to be side-effect free. This makes it easier to write correct programs, and to compose large programs from smaller ones. Clojure is **concurrent**. Rather than error-prone locking, Clojure provides software transactional memory. Clojure **embraces Java**. Calling from Clojure to Java is direct, and goes through no translation layer. Clojure is **fast**. Wherever you need it, you can get the exact same performance that you could get from hand-written Java code.

I've been programming in Lisp for a while, then moved to Python in order to use something less dated and to be able to do more agile web development. But the strengths of Lisp, together with that kind of magic that comes with it (maybe coming from the [code-as-data paradigm](http://en.wikipedia.org/wiki/Homoiconicity)) is something which I bet all Lisp programmers miss in other languages. So I decided to give Clojure a go..

Installation is surprisingly super easy - and I mean it - especially if you are on mac osX. Clojure is a java library, so all you have to do is [download the package and run it from the command line using your java compiler](http://clojure.org/getting_started). That gives you the basic interactive environment:

```

java -cp clojure.jar clojure.main
```

The interpreter is good for testing, but not for building large programs. So the next step is getting an IDE. Looks like there are [many choices available](http://www.bestinclass.dk/index.clj/2010/03/clojure-ides-the-grand-tour-getting-started.html), so just pick one of your liking. I personally love [TextMate](http://macromates.com/) a lot, so I was happy to find out that there is a [clojure bundle](https://github.com/swannodette/textmate-clojure) that contains all that you need to get started (yes, the clojure environment too, so you can even skip the step above). Easy beasy to install, but first you need to install [Cake](https://github.com/ninjudd/cake), a build tool that you can get via ruby's gem command (usually preinstalled on OSx). So:

```

sudo gem install cake
```

Then install Textmate's bundle for clojure like this:

```

$ cd ~/Library/Application Support/TextMate/Bundles
$ git clone git://github.com/swannodette/textmate-clojure.git Clojure.tmbundle
$ osascript -e 'tell app "TextMate" to reload bundles'
```

I don't use Ruby, so the final step for me was adding to the system path the location of ruby's gems (so that Cake can be run from Textmate). Open up you ~/.bash\_profile and add this line:

```

export PATH="/Users/mike/.gem/ruby/1.8/bin:$PATH"
```

That's it! A nice fellow created a really good video tutorial about how to use Textmate with the Clojure bundle, so I was able to run my first application quite quickly:

Once you've familiarized with the environment, copy and paste the code below - it's an implementation of the Tetris game in clojure (which I found [here](https://github.com/yogthos/Clojure-Tetris/blob/master/src/tetris.clj)). Very useful as a learning resource!

(ns tetris
  (:import
    (javax.swing JFrame)
    (java.awt Canvas Graphics Color Toolkit)
    (java.awt.event ActionListener KeyListener KeyEvent))
  (:gen-class))

(def **\*cols\*** 10)
(def **\*rows\*** 20)
(def **\*width\*** 300)
(def **\*height\*** 600)
(def **\*offset\*** (**atom** \[0, 0\]))
(def **\*rotation\*** (**atom** **nil**))
(def **\*shapes\***  \[\[\[0,1\],\[0,2\],\[0,3\],\[0,4\]\]
                \[\[0,0\],\[0,1\],\[1,1\],\[1,2\]\]
                \[\[1,2\],\[1,1\],\[0,1\],\[0,0\]\]
                \[\[0,0\],\[0,1\],\[1,0\],\[1,1\]\]
                \[\[0,0\],\[0,1\],\[0,2\],\[1,2\]\]
                \[\[1,0\],\[1,1\],\[1,2\],\[0,2\]\]\])

(defn get-shape \[\]
  (**let** \[shape (rand-nth **\*shapes\***)
        offset (inc (rand-int (**\-** **\*cols\*** 3)))\]
    (**map** (fn \[\[x y\]\] \[(**+** x offset), y\]) shape)))

(defn get-board \[\]
  (vec (range (**\*** **\*rows\*** **\*cols\***))))

(defn pos-to-xy \[pos\]
  (**let** \[x (**mod** pos **\*cols\***)
        y (int (**/** (**\-** pos x) **\*cols\***))\]
    \[x, y\]))

(defn collides?
  (\[board x y pos\]
    (**let** \[\[posx posy\] (pos-to-xy pos)\]
      (**and**
        (**\>** x (**\-** 1))
        (**<** x **\*cols\***)
        (**<** y **\*rows\***)
        (**not** (**and**
              (**\=** posx x)
              (**\=** posy y)
              (**not** (**get** board (**+** pos **\*cols\***))))))))
  (\[board shape pos\]
    (**every**?
      #{true}
      (for \[\[x y\] shape\]
       (collides? board x y pos))))
  (\[board shape\]
    (**not** (**reduce**
           #(**and** %1 (collides? board shape %2))
          (range (**count** board)))) ))

(defn rotate \[board shape\]
  (**if** (**nil**? @\*rotation\*)
    shape
    (**let** \[\[avg-x avg-y\] (\->> shape
                          (**reduce**
                            (fn \[\[tx ty\] \[x y\]\]
                              \[(**+** tx x), (**+** ty y)\]))
                          (**map** #(int (**/** % 4))))

          rotated (**map** (fn \[\[x y\]\]
                         \[(int (**+** avg-x (**\-** y avg-y)))
                          (int (**\-** avg-y (**\-** x avg-x)))\])
                    shape)\]
      (**if** (collides? board rotated)
        shape rotated))))

(defn shift \[board shape\]
  (**let** \[shifted (**map**
                  (fn \[\[x y\]\]
                    \[(**+** x (**first** @\*offset\*)), y\])
                  shape)\]
    (**if** (collides? board shifted)
      shape shifted)))

(defn transform \[board shape drop?\]
  (**let** \[shifted (shift board shape)
        rotated (rotate board shifted)\]
    (**if** drop?
      (**map** (fn \[\[x y\]\]
             \[x, (**if** drop? (inc y) y)\]) rotated)
      rotated)))

(defn clear-lines \[board\]
  (**let** \[new-board (**apply** concat
                    (filter #(**some** #{true} %)
                      (partition **\*cols\*** board)))\]
    (into
      (vec (**map** (fn \[\_\] true)
             (range (**\-** (**count** board) (**count** new-board)))))
      new-board)))

(defn update-board \[board shape\]
  (vec (**map** #(**let** \[\[x y\] (pos-to-xy %)\]
               (**if** (**some**
                     (fn \[\[px py\]\] (**and**(**\=** x px) (**\=** y py)))
                     shape)
                 false (**get** board %)))
         (range (**count** board)))))

(defn game-over? \[board\]
  (**not** (**reduce** #(**and** %1 %2)
         (**butlast** (**rest** (take **\*cols\*** board))))))

;;;;;;Controls;;;;
(def **\*dirs\*** {KeyEvent/VK\_LEFT  \[-1, 0\]
             KeyEvent/VK\_RIGHT \[1, 0\]
             KeyEvent/VK\_UP :left
             KeyEvent/VK\_DOWN :right})

(defn handle-input \[#^KeyEvent event\]
  (**let** \[key (.getKeyCode event)\]
    (**cond**
      (**or** (**\=** key KeyEvent/VK\_LEFT) (**\=** key KeyEvent/VK\_RIGHT))
      (**let** \[disp (**\*dirs\*** key)\]
        (**when** disp (swap! **\*offset\*** #(**map** **+** disp %))))
      (**or** (**\=** key KeyEvent/VK\_UP) (**\=** key KeyEvent/VK\_DOWN))
      (reset! **\*rotation\*** (**\*dirs\*** key)))))

(defn input-listener \[\]
  (proxy \[ActionListener KeyListener\] \[\]
    (actionPerformed \[e\])
    (keyPressed \[e\] (handle-input e))
    (keyReleased \[e\])
    (keyTyped \[e\])))

;;;;;;;UI;;;;;;;;;
(defn draw \[#^Canvas canvas draw-fn\]
  (**let** \[buffer  (.getBufferStrategy canvas)
        g       (.getDrawGraphics buffer)\]
    (try
      (draw-fn g)

      (finally (.dispose g)))
    (**if** (**not** (.contentsLost buffer))
      (. buffer show))
    (.. Toolkit (getDefaultToolkit) (sync))))

(defn draw-square \[x y #^Graphics g\]
  (**let** \[width  (**/** **\*width\*** **\*cols\***)
        height (**/** **\*height\*** **\*rows\***)
        xpos   (**\*** x width)
        ypos   (**\*** y width)\]
    (doto g
      (.setColor Color/RED)
      (.fillRect xpos, ypos, width, height)
      )))

(defn draw-game-over \[#^Graphics g\]
  (doto g
   (.setColor Color/BLACK)
   (.fillRect 0 0 **\*width\*** **\*height\***)
   (.setColor Color/green)
   (.drawString "GAME OVER" (**\-** (**/** **\*width\*** 2) 50)  (**/** **\*height\*** 2))))

(defn draw-board \[board shape\]
  (fn \[#^Graphics g\]
    (doto g
      (.setColor Color/BLACK)
      (.fillRect 0 0 **\*width\*** **\*height\***))

    (doseq \[square (range (**count** board))\]
      (**when** (**not** (**get** board square))
       (**let** \[\[x y\] (pos-to-xy square)\]
         (draw-square x y g))))

    (doseq \[\[x y\] shape\]
      (draw-square x y g))))

(defn -main \[& args\]
  (**let** \[frame  (JFrame. "Tetris")
        canvas (Canvas.)\]
    (doto frame
      (.setSize **\*width\*** (**+** (**/** **\*height\*** **\*rows\***) **\*height\***))
      (.setDefaultCloseOperation JFrame/EXIT\_ON\_CLOSE)
      (.setResizable false)
      (.add canvas)
      (.setVisible true))

    (doto canvas
      (.createBufferStrategy 2)
      (.addKeyListener (input-listener))
      (.setVisible true)
    (.requestFocus))

    ;;game loop
    (**loop** \[board    (get-board)
           shape    (get-shape)
           old-time (System/currentTimeMillis)\]

      (reset! **\*offset\*** \[0,0\])
      (reset! **\*rotation\*** **nil**)
      (Thread/sleep 10)
      (draw canvas (draw-board board shape))

      (**let** \[cur-time (System/currentTimeMillis)
            new-time (long (**if** (**\>** (**\-** cur-time old-time) 150)
                             cur-time
                             old-time))
            drop?    (**\>** new-time old-time)\]
        (**cond**
          (game-over? board)
          (draw canvas draw-game-over)

          (collides? board shape)
          (recur (update-board board shape)
            (get-shape)
          new-time)

          **:default**
          (recur
            (clear-lines board)
            (transform board shape drop?)
            new-time)
          )))))
(\-main)

Quite amazing isn'it? However, the very next question for me was, why investing time and money into this new language? It's definitely interesting, but does it compare to python and django (for example) when it comes to build social web apps? Can't really answer to these questions at the moment, but I found really useful the conclusions of an article I found online (on [Java News Brief](http://java.ociweb.com/mark/clojure/article.html)):

> • Are you looking for a way to make concurrent programming easier? • Are you open to branching outside the world of object-oriented programming to try functional programming? • Is it important for the applications you write to run on the JVM in order to take advantage of existing Java libraries, portability and other benefits? • Do you prefer dynamically-typed languages over statically-typed ones? • Do you find the minimal, consistent syntax of Lisp dialects appealing? If you answered "yes" some of these questions then you should consider using Clojure as your next programming language.

Finally, a couple of other useful learning resources:

\- [setting up clojure on mac osX Leopard](http://mark.reid.name/sap/setting-up-clojure.html) - [clojure for lisp programmers](http://clojure.blip.tv/) (video lecture) - [Clojure Tutorial For the Non-Lisp Programmer](http://www.moxleystratton.com/article/clojure/for-non-lisp-programmers) - a clojure [implementation of the snake game](http://java.ociweb.com/mark/clojure/ClojureSnake.html)

...
