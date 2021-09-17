---
title: "Pyglet: multimedia library for python"
date: "2009-12-12"
categories: 
  - "techlife"
tags: 
  - "graphics"
  - "multimedia"
  - "python"
  - "sound"
---

UPDATE 30/03/1: Just realized that unfortunately pyglet doesn't play well with the latest 64bit architecture of oSX. A real shame, as this obviously breaks Pyglet's famed run-anywhere feature. There are reasons to think that the next version will fix this problem (check out [this thread](http://code.google.com/p/pyglet/issues/detail?id=438) for more info).. but for the moment, I guess that the only alternative is falling back to [PyOpenGl](http://pyopengl.sourceforge.net/). UPDATE 14/12/09: [pyProcessing](http://code.google.com/p/pyprocessing/) is a project building on pyglet that that creates an environment for graphics applications that closely resembles that of the [Processing](http://www.processing.org/) system. Quite neat uh?

**[Pyglet](http://www.pyglet.org/index.html)** provides an object-oriented programming interface for developing games and other visually-rich applications for Windows, Mac OS X and Linux. I've been playing with it for an hour or so, and was surprised of how **quickly** it can let you create a python-based multimedia application.

Some of the features of pyglet are:

> **No external dependencies or installation requirements**. For most application and game requirements, pyglet needs nothing else besides Python, simplifying distribution and installation. **Take advantage of multiple windows and multi-monitor desktops.** pyglet allows you to use as many windows as you need, and is fully aware of multi-monitor setups for use with fullscreen games. **Load images, sound, music and video in almost any format.** pyglet can optionally use AVbin to play back audio formats such as MP3, OGG/Vorbis and WMA, and video formats such as DivX, MPEG-2, H.264, WMV and Xvid.

Two possibly useful tips when getting started:

\- Go get [**AVBIN**](http://code.google.com/p/avbin/) without hesitations, as you'll need it. **MP3** and other compressed audio formats **require** AVbin to be **installed** (this is the default for the Windows and Mac OS X installers). Uncompressed WAV files can be played without AVbin.

\- \[_tested on **OSx leopard** only_\] If you try running the **hello-world example** from the console, after hitting _window = pyglet.window.Window()_ you'll see a new window appearing on your screen. That looks like good news obviously, but soon you'll find out that the **Finder doesn't like that**, and apparently the Python launcher results being as 'not responding' on the Force Quit Application menu. Well nothing to worry there: it's because you haven't issued the _pyglet.app.run()_ command yet (which is where the main event loop gets handled).

[![](http://www.michelepasin.org/blog/wp-content/uploads/2009/12/screen-shot-2009-12-12-at-21-06-22.png?w=300 "Screen shot 2009-12-12 at 21.06.22")](http://www.michelepasin.org/blog/wp-content/uploads/2009/12/screen-shot-2009-12-12-at-21-06-22.png)

The screenshot above is taken from one of the example apps you can download. Balls keeps bouncing around in a window, playing a sound when they hit the border. Check out the code:

import os
import random
import sys

from pyglet.gl import \*
import pyglet
from pyglet.window import key

BALL\_IMAGE \= 'ball.png'
BALL\_SOUND \= 'ball.wav'

if len(sys.argv) \> 1:
    BALL\_SOUND \= sys.argv\[1\]

sound \= pyglet.resource.media(BALL\_SOUND, streaming\=False)

class Ball(pyglet.sprite.Sprite):
    ball\_image \= pyglet.resource.image(BALL\_IMAGE)
    width \= ball\_image.width
    height \= ball\_image.height

    def \_\_init\_\_(self):
        x \= random.random() \* (window.width \- self.width)
        y \= random.random() \* (window.height \- self.height)

        super(Ball, self).\_\_init\_\_(self.ball\_image, x, y, batch\=balls\_batch)

        self.dx \= (random.random() \- 0.5) \* 1000
        self.dy \= (random.random() \- 0.5) \* 1000

    def update(self, dt):
        if self.x \= window.width:
            self.dx \*\= \-1
            sound.play()
        if self.y \= window.height:
            self.dy \*\= \-1
            sound.play()
        self.x +\= self.dx \* dt
        self.y +\= self.dy \* dt

        self.x \= min(max(self.x, 0), window.width \- self.width)
        self.y \= min(max(self.y, 0), window.height \- self.height)

window \= pyglet.window.Window(640, 480)

@window.event
def on\_key\_press(symbol, modifiers):
    if symbol \=\= key.SPACE:
        balls.append(Ball())
    elif symbol \=\= key.BACKSPACE:
        if balls:
            del balls\[\-1\]
    elif symbol \=\= key.ESCAPE:
        window.has\_exit \= True

@window.event
def on\_draw():
    window.clear()
    balls\_batch.draw()
    label.draw()

def update(dt):
    for ball in balls:
        ball.update(dt)
pyglet.clock.schedule\_interval(update, 1/30.)

balls\_batch \= pyglet.graphics.Batch()
balls \= \[\]
label \= pyglet.text.Label('Press space to add a ball, backspace to remove',
                          font\_size\=14,
                          x\=window.width // 2, y\=10,
                          anchor\_x\='center')

if \_\_name\_\_ \=\= '\_\_main\_\_':
    pyglet.app.run()
