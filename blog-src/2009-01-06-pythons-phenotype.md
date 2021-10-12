---
title: "Python's phenotype"
date: "2009-01-06"
categories: 
  - "justblogging"
  - "techlife"
tags: 
  - "code"
  - "python"
---

Phenotype: _any observable characteristic or trait of an organism: such as its morphology, development, biochemical or physiological properties, or behavior_.

```python
>>> type('aaa') 
<type 'str'> 
>>> type('aaa') == type('a') 
True 
>>> type(type('aaa') == type('a')) 
<type 'bool'> 
>>> type(type(type('aaa') == type('a'))) 
<type 'type'> 
>>> type(type(type(type('aaa') == type('a')))) 
<type 'type'> 
>>> type(type(type(type(type('aaa') == type('a'))))) 
<type 'type'>
```

If you don’t know what’s going on, I’ve just been fooling around with python's [type system](http://www.cafepy.com/article/python_types_and_objects/python_types_and_objects.html) and [IDLE](https://docs.python.org/3/library/idle.html)
