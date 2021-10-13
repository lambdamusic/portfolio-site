---
title: "Introducing DimCli: a Python CLI for the Dimensions API"
date: "2019-05-24"
categories: 
  - "data-science"
  - "techlife"
tags: 
  - "api"
  - "cli"
  - "dimensions"
  - "python"
  - "scholarly-analytics"
---

For the last couple of months I've been working on a new open source Python project. This is called **DimCli**  and it's a command-line library aimed at making it simpler to work with the Dimensions Analytics API.

The project is [available on Github](https://github.com/lambdamusic/dimcli). In a nutshell, DimCli helps people becoming productive with the powerful scholarly analytics API from Dimensions. See the video below for a quick taster of the functionalities available.

<iframe width="560" height="315" src="https://www.youtube.com/embed/HbZPxJ7G_00?controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Background

I recenlty joined the [Dimensions](https://www.dimensions.ai/) team, so needed a way to get to grips with their feature-rich API ([official docs](https://docs.dimensions.ai/dsl)). So, building DimCli has been a fun way for me to dig into the logic of the **Dimensions Search Language** (DSL).

Plus, this project gave me a chance to learn more about two awesome Python technologies: [JupyterLab](https://github.com/jupyterlab/jupyterlab) and its magic commands, as well as the [Python Prompt Toolkit](https://python-prompt-toolkit.readthedocs.io/en/stable/) library.

[![](/media/static/blog_img/Screenshot-2019-05-24-dimcli.png)](/media/static/blog_img/Screenshot-2019-05-24-dimcli.png)

### Features, at a glance

- DimCli is an **interactive** **query console** for the Dimensions Analytics API (ps: [Dimensions](https://www.dimensions.ai/) is a world-class research-data platform including information about millions of documents like publications, patents, grants, clinical trials and policy documents.
- It **helps** **learning the Dimensions Search Language (DSL)** thanks to a built-in autocomplete and documentation search mechanism.
- It handles **authentication** transparently either via a global user-specific credentials file, or by passing credentials manually (e.g. when used within shared environments).
- It allows to **export results to CSV, JSON and pandas dataframes**, hence making it easier to integrate with other data analysis tools.
- It is **compatible with Jupyter**, e.g. it includes various magic commands that make it super simple to interrogate Dimensions ([various examples here](https://github.com/digital-science/dimensions-api/tree/master/1.Getting%20Started)).

```python
>>> import dimcli

>>> dimcli.login(username="mary.poppins", password="chimneysweeper")

>>> dsl = dimcli.Dsl()

>>> res = dsl.query("""search grants for "malaria" return researchers""")

>>> print(res.json)
{'researchers': [{'id': 'ur.01332073522.49',
   'count': 75,
   'last_name': 'White',
   'first_name': 'Nicholas J'},
  {'id': 'ur.01343654360.43',
   'count': 59,
   'last_name': 'Marsh',
   'first_name': 'Kevin'},
  .............
  ],
 '_stats': {'total_count': 8735}}
```


### Feedback

DimCli lives on [Github](https://github.com/lambdamusic/dimcli), so for any feedback or bug reports, feel free to open an issue there.

![](/media/static/blog_img/Screenshot 2019-05-23 at 18.06.32.png)
