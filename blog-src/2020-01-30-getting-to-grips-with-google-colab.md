---
title: "Getting to grips with Google Colab"
date: "2020-01-30"
categories: 
  - "data-science"
  - "techlife"
tags: 
  - "googlecolab"
  - "jupyter"
---

I've been using Google Colab on a regular basis during the last few months, as I was curious to see whether I could make the switch to it (from a more traditional Jupyter/Jupyterlab environment). As it turns out, Colab is pretty amazing in many respects but there are still situations where a local Jupyter notebook is my first choice. Keep reading to discover why!

### Google Colab VS Jupyter

[Google Colaboratory](https://colab.research.google.com/) (also known as Colab, see the [faqs](https://research.google.com/colaboratory/faq.html)) is a free [Jupyter](https://en.wikipedia.org/wiki/Project_Jupyter) notebook environment that runs in the cloud and stores its notebooks on Google Drive.

Colab has become extremely popular with data scientists and in particular people doing some kind of **machine learning tasks**. Party, I guess, that's because Colab has deep integration with Google's ML tools (eg [Tensorflow](https://en.wikipedia.org/wiki/TensorFlow)) and in fact Colab actually permits to switch to a [Tensor Processing Unit](https://en.wikipedia.org/wiki/Tensor_processing_unit) (TSU) when running your notebook.  For FREE. . Which, by itself, is pretty remarkable already.

There are tons of videos on [Youtube](https://www.youtube.com/results?search_query=google+colab) and tutorials on [Medium](https://towardsdatascience.com/search?q=google%20colab), so I'm not gonna describe it any further, because there is definitely no shortage of learning materials if you want to find out more about it.

<iframe width="560" height="315" src="https://www.youtube.com/embed/inN8seMm7UI?controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### How I'm using Colab

I normally turn to notebooks because I need to demonstrate real-world applications of APIs to a (sometimes not-so-technical) audience. A lot of the work I've been doing lately has crystallized into the '[Dimensions API Labs](https://digital-science.github.io/dimensions-api-lab/)' portal. This is essentially a collection of notebooks aimed at making it easier for people to extract, process and turn into actionable insights the many kinds of data my company's APIs can deliver.

My usual **workflow**:

- Getting some data by calling APIs, sometimes using custom-built Python packages;
- Processing the data using [pandas](https://en.wikipedia.org/wiki/Pandas_(software)) or built-in Python libraries;
- Building visualizations and summaries e.g. using [Plotly](https://plot.ly/python/).

My target **audience**:

- Data scientist and developers who want to become proficient with our APIs.
- Analysts and domain experts who are less technically advanced, but have the capacity to turn interesting research questions into queries and API-based workflows.

Read on to find out how Colab ticked a lot of the boxes for this kind of work.

### Pros of Colab

In general, Jupyter notebooks are an ideal tool for showcasing API functionalities and data features. The ability to pack together code, images and text within a single runnable file make the end result intuitive yet powerful.

Google Colab brings a number of extra benefits to the table:

1. **No install set up.**  That was a massive selling point for me. If I have to share an API recipe with just anyone, Colab allows to do that very very quickly, even with non technical users. They just have to open up a webpage, hit ‘play’ and run the notebook. Moreover, Colab includes by default many popular Python libraries and, if you need to, you can pip-install your own favorite ones too. Neat!
2. **It scales well.** I ran a couple of workshop recently with 30+ users, without any performance issue. E.g. compared to setting up a Jupyterhub server, it's much easier,  and cheaper too, of course. Plus, people can go home and re-run the same notebooks virtually withing the same exact environment. No need to fiddle with Python, Docker or Jupyter packages.
3. **Sharing and commenting.** The collaborative features of Colab need no introduction. Just think of how easy it is to share a Google Doc with your colleagues, only in this case you'd do it with a notebook!
4. **Playground mode.** Colab introduced the notion of [playground mode](https://stackoverflow.com/questions/52011084/what-is-playground-mode-in-googles-colaboratory), which essentially allows you to open a notebook in read-only mode (trying to save throws the error "_This notebook is in playground mode. Changes will not be saved unless you make a copy of the notebook."_). I find this feature extremely handy for demos, or in situations where one needs to mess about with a notebook without the risk of overwriting its 'stable' state.
5. **Snippets**. Colab includes a sidebar with many useful code snippets by default. You can extend that easily by [creating your own 'snippets' notebook](https://stackoverflow.com/questions/48760503/is-there-a-way-to-add-your-own-snippets-in-google-colaboratory), going to _Tools > Preferences_, paste the snippets notebook URL in Custom snippet notebook URL and save. Simple and effective. And the new snippets can be shared with team mates too!
6. **Extra UI components.** The Colab folks developed a syntax for generating [Forms components using markdown](https://colab.research.google.com/notebooks/forms.ipynb).  This is very cool because it lets you generate simple input boxes, which can  be used for example by non technical people to enter data into a notebook. Also worth pointing out that forms are created using comments-like code (eg `#@param {type:"string"})` so they don't interfere with the notebook if you open it within a traditional Jupyter environment.
7. **The Google ecosystem.** The integration with the rest of the G-Suite is unsurprisingly amazing so pulling/putting data in and out of [Drive, Sheets or BigQuery](https://colab.research.google.com/notebooks/io.ipynb)  is quick, easy and well-documented.

### Cons of Colab

1. **Performance limitations.** Of course the performance will never be as good as running things locally (having said that - you can even use GPUs for free, but haven’t tried that yet). So for bigger projects e.g. involving complex algorithms or very large datasets, other data science platforms are probably better eg [Gigantum](https://gigantum.com/)
2. **Interface learning.** You have to get used to the Colab interface. It somehow still feels a bit more fiddly than JupyterLab, to me. Keyword shortcuts can be a problem too: you can customize them in Colab, but I couldn't replicate all of my (rather heavily customized) JupyterLab ones, due to conflicts with other default ones in Colab. So some muscle-memory pain there.
3. **Exporting to HTML is not that good.** Being able to turn Jupyter notebooks into a simple HTML file is pretty handy, but Colab can't do that. You can of course download the ._ipynb_ file and then export locally (via [nbconvert](https://github.com/jupyter/nbconvert)), but that doesn't always produce the results you'd expect either. For example, Plotly visualizations (like [this one](https://digital-science.github.io/dimensions-api-lab/cookbooks/8-organizations/2-Industry-Collaboration.html#Putting-Countries-and-Collaborators-together%E2%80%A6)) are not rendering properly unless I run the whole notebook locally in Jupyterlab before exporting.
4. **Some Python libraries won't work out of the box.** For example I have a Python library called [dimcli](https://github.com/digital-science/dimcli) that builds on the latest [prompt-toolkit](https://python-prompt-toolkit.readthedocs.io/en/master/). Turns out that Colab, by default, runs ipython 5.5.0 (latest version is 7), which is incompatible with promt-toolkit. You can of course uprade everything on Colab (eg _pip install --upgrade --force-reinstall library-name_) - which is great - however that may lead to further dependencies errors.. and so on.
5. **Project versioning.** Colab includes a built-in [revision history](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb) tool, and it can integrate with [Github](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb) too.  Yet, I often end up creating multiple copies/versions of a notebook, instead of relying on the revisions system. I wish there was a better way to do this..
6. **The Google ecosystem (AGAIN).** As much as this can be a massive plus for some people (see above), it can also be a massive problem for others. Some customers I work with don't have access to G-Suite, full stop. That's not so uncommon, especially with large enterprises that are concerned about data privacy.

### Conclusion: Colab and JupyterLab need to co-exist

**Google Colab is simply great for small/medium data projects**. Hands down to the developers who built it. Some features are totally neat, and especially when I intend to share whatever I'm doing with more than one person, I hit right away my [New Colab Document](https://colab.research.google.com/notebook#create=true&language=python3) shortcut.

Nonetheless, **I still use [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) a lot**, for a variety of projects. E.g. for quick personal data investigations. Or for projects that I know will be shared only with other data scientists (who need no guidance in order to run them). Or in projects with long-running processes and memory consumption.

So the two things **need to coexist**. 

### Not so easy though..

Which opens up a new problem: _how to seamlessly move from one environment to the other_? That's still an open question for me, but you'll find what I learned so far in what follows.

1. I try to put all of my notebooks in Google Drive, so that they are accessible by Colab.
1. I sync my Google Drive to my laptop, so I've got everything locally as well (ps: I sync Drive to _one computer only_ so to avoid double/out-of-sync issues).
1. I have several folders containing notebooks. Some of these folders are actually Github repositories too. They seem to sync over Drive without issues (so far!)
1. This setup means that **I can either work on Colab (thanks to Drive) or local Jupyter (via the local sync) depending on my needs**. I can even start working on something locally and then complete it on Colab. The .ipynb files are 100% compatible (almost - see above the exception about rendered visualizations)
1. Any Colab-specific code does not break Jupyter. There is some redundancy on occasions (eg _pip installing_ libraries on Colab which I already have on my laptop) but that's fine. It's also possible to use expressions like this \`_if not 'google.colab' in sys.modules_\` to run code selectively based on the platform (eg see [here](https://digital-science.github.io/dimensions-api-lab/cookbooks/8-organizations/2-Industry-Collaboration.html#Load-libraries-and-log-in)).

 
Makes sense? If you know of a better way to do this I'd love to know. 