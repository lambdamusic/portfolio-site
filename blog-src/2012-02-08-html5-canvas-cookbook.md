---
title: "HTML5 Canvas Cookbook"
date: "2012-02-08"
categories: 
  - "techlife"
tags: 
  - "book"
  - "canvas"
  - "html5"
---

[HTML5 Canvas Cookbook](http://www.packtpub.com/html5-canvas-cookbook-recipes-to-revolutionize-web-experience/book) is a new publication from Packt publishing that discusses in details the new drawing functionalities the html5 canvas element makes available; in the last weeks I've been looking at this book in more details and since it's been a quite useful learning experience I wanted to mention it here too.

The book (which is [available online here](http://www.packtpub.com/html5-canvas-cookbook-recipes-to-revolutionize-web-experience/book) )is simple and well organized; it spends quite a bit of time on both introductory topics and more advanced ones, so it'll probably fit both the beginner and the more experienced programmer.

Here's a list of the chapters available:

CHAPTER 1: GETTING STARTED WITH PATHS AND TEXT
Introduction
Drawing a line
Drawing an arc
Drawing a Quadratic curve
Drawing a Bezier curve
Drawing a zigzag
Drawing a spiral
Working with text
Drawing 3D text with shadows
Unlocking the power of fractals: Drawing a haunted tree

CHAPTER 2: SHAPE DRAWING AND COMPOSITES
Introduction
Drawing a rectangle
Drawing a circle
Working with custom shapes and fill styles
Fun with Bezier curves: drawing a cloud
Drawing transparent shapes
Working with the context state stack to save and restore styles
Working with composite operations
Creating patterns with loops: drawing a gear
Randomizing shape properties: drawing a field of flowers
Creating custom shape functions: playing card suits
Putting it all together: drawing a jet

CHAPTER 3: WORKING WITH IMAGES AND VIDEOS
Introduction
Drawing an image
Cropping an image
Copying and pasting sections of the canvas
Working with video
Getting image data
Introduction to pixel manipulation: inverting image colors
Inverting video colors
Converting image colors to grayscale
Converting a canvas drawing into a data URL
Saving a canvas drawing as an image
Loading the canvas with a data URL
Creating a pixelated image focus

CHAPTER 4: MASTERING TRANSFORMATIONS
Introduction
Translating the canvas context
Rotating the canvas context
Scaling the canvas context
Creating a mirror transform
Creating a custom transform
Shearing the canvas context
Handling multiple transforms with the state stack
Transforming a circle into an oval
Rotating an image
Drawing a simple logo and randomizing its position, rotation, and scale

CHAPTER 5: BRINGING THE CANVAS TO LIFE WITH ANIMATION
Introduction
Creating an Animation class
Creating a linear motion
Creating acceleration
Creating oscillation
Oscillating a bubble
Swinging a pendulum
Animating mechanical gears
Animating a clock
Simulating particle physics
Creating microscopic life forms
Stressing the canvas and displaying the FPS

CHAPTER 6: INTERACTING WITH THE CANVAS: ATTACHING EVENT LISTENERS TO SHAPES AND REGIONS 
Introduction
Creating an Events Class
Working With Canvas Mouse Coordinates
Attaching Mouse Event Listeners to Regions
Attaching Touch Event Listeners to Regions on a Mobile Device
Attaching Event Listeners to Images
Dragging-And-Dropping Shapes
Dragging-And-Dropping Images
Creating an Image Magnifier
Creating a Drawing Application

CHAPTER 7: CREATING GRAPHS AND CHARTS
Introduction
Creating a pie chart
Creating a bar chart
Graphing equations
Plotting data points with a line chart

CHAPTER 8: SAVING THE WORLD WITH GAME DEVELOPMENT
Introduction
Creating sprite sheets for the heroes and enemies
Creating level images and boundary maps
Creating an Actor class for the hero and enemies
Creating a Level class
Creating a Health Bar class
Creating a Controller class
Creating a Model class
Creating a View class
Setting up the HTML document and starting the game

CHAPTER 9: INTRODUCING WEBGL
Introduction
Creating a WebGL wrapper to simplify the WebGL API
Creating a triangular plane
Rotating a triangular plane in 3D space
Creating a rotating cube
Adding textures and lighting
Creating a 3D world that you can explore

The last chapters about animations and game developments are probably the most interesting ones, especially they all include detailed walk-through of the techniques discussed. Here's for example an example from Chapter 5, 'Oscillating a bubble':

\[inline\]

\[script type="text/javascript"\]

var Animation = function(canvasId){ this.canvas = document.getElementById(canvasId); this.context = this.canvas.getContext("2d"); this.t = 0; this.timeInterval = 0; this.startTime = 0; this.lastTime = 0; this.frame = 0; this.animating = false; // provided by Paul Irish window.requestAnimFrame = (function(callback){ return window.requestAnimationFrame || window.webkitRequestAnimationFrame || window.mozRequestAnimationFrame || window.oRequestAnimationFrame || window.msRequestAnimationFrame || function(callback){ window.setTimeout(callback, 1000 / 60); }; })(); };

Animation.prototype.getContext = function(){ return this.context; };

Animation.prototype.getCanvas = function(){ return this.canvas; };

Animation.prototype.clear = function(){ this.context.clearRect(0, 0, this.canvas.width, this.canvas.height); };

Animation.prototype.setDrawStage = function(func){ this.drawStage = func; };

Animation.prototype.isAnimating = function(){ return this.animating; };

Animation.prototype.getFrame = function(){ return this.frame; };

Animation.prototype.start = function(){ this.animating = true; var date = new Date(); this.startTime = date.getTime(); this.lastTime = this.startTime; if (this.drawStage !== undefined) { this.drawStage(); } this.animationLoop(); };

Animation.prototype.stop = function(){ this.animating = false; }; Animation.prototype.getTimeInterval = function(){ return this.timeInterval; };

Animation.prototype.getTime = function(){ return this.t; };

Animation.prototype.getFps = function(){ return this.timeInterval > 0 ? 1000 / this.timeInterval : 0; };

Animation.prototype.animationLoop = function(){ var that = this; this.frame++; var date = new Date(); var thisTime = date.getTime(); this.timeInterval = thisTime - this.lastTime; this.t += this.timeInterval; this.lastTime = thisTime; if (this.drawStage !== undefined) { this.drawStage(); } if (this.animating) { requestAnimFrame(function(){ that.animationLoop(); }); } };

window.onload = function(){ // instantiate new animation object var anim = new Animation("myCanvas"); var context = anim.getContext(); var canvas = anim.getCanvas(); anim.setDrawStage(function(){ // update var widthScale = Math.sin(this.getTime() / 200) \* 0.1 + 0.9; var heightScale = -1 \* Math.sin(this.getTime() / 200) \* 0.1 + 0.9;

// clear this.clear(); //draw context.beginPath(); context.save(); context.translate(canvas.width / 2, canvas.height / 2); context.scale(widthScale, heightScale); context.arc(0, 0, 65, 0, 2 \* Math.PI, false); context.restore(); context.fillStyle = "#8ED6FF"; context.fill(); context.lineWidth = 2; context.strokeStyle = "#555"; context.stroke(); context.beginPath(); context.save(); context.translate(canvas.width / 2, canvas.height / 2); context.scale(widthScale, heightScale); context.arc(-30, -30, 15, 0, 2 \* Math.PI, false); context.restore(); context.fillStyle = "white"; context.fill(); }); anim.start(); };

\[/script\]

\[/inline\]

In a nutshell, this is what is going on (note that the 'animation' library is discussed in a previous chapter of the book):

<script src\="animation.js"\></script\>
<script\>
    window.onload \= function(){
        // instantiate new animation object
        var anim \= new Animation("myCanvas");
        var context \= anim.getContext();
        var canvas \= anim.getCanvas();
        
        anim.setDrawStage(function(){
            // update
            var widthScale \= Math.sin(this.getTime() / 200) \* 0.1 + 0.9;
            var heightScale \= \-1 \* Math.sin(this.getTime() / 200) \* 0.1 + 0.9;

            // clear
            this.clear();
            
            //draw
            context.beginPath();
            context.save();
            context.translate(canvas.width / 2, canvas.height / 2);
            context.scale(widthScale, heightScale);
            context.arc(0, 0, 65, 0, 2 \* Math.PI, false);
            context.restore();
            context.fillStyle \= "#8ED6FF";
            context.fill();
            context.lineWidth \= 2;
            context.strokeStyle \= "#555";
            context.stroke();
            
            context.beginPath();
            context.save();
            context.translate(canvas.width / 2, canvas.height / 2);
            context.scale(widthScale, heightScale);
            context.arc(\-30, \-30, 15, 0, 2 \* Math.PI, false);
            context.restore();
            context.fillStyle \= "white";
            context.fill();
        });
        
        anim.start();
    };
</script\>

All in all, a book definitely worth reading!
