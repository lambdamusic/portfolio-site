---
title: "Running interactive Jupyter demos with  mybinder.org"
date: "2019-05-03"
categories: 
  - "data-science"
tags: 
  - "jupyter"
  - "notebooks"
  - "sharing"
---

The online tool [mybinder.org](https://mybinder.org/) allows to turn a Git repo into a collection of interactive notebooks with one click.

I played with it a little today and was pretty impressed! A very useful tool e.g. if you have a repository of Jupyter notebooks and want to showcase them to someone with no access to a Jupyter environment.

[![](/media/static/blog_img/Screenshot-2019-05-03-binder.png)](Screenshot-2019-05-03-binder.png)

I was able to run many of the [Dimensions API notebooks](https://github.com/digital-science/dimensions-api) I've been working on in the last months, with little or no changes (follow [this link to try them](https://hub.mybinder.org/user/digital-science-dimensions-api-y3409gua/tree) yourself). Dependencies can be loaded on the fly, and new files (eg local settings) create just as if you are working within a normal Jupyter notebook.

[![](/media/static/blog_img/Screenshot-2019-05-03-binder2.png)](Screenshot-2019-05-03-binder2.png)

> See the official [docs](https://mybinder.readthedocs.io/en/latest/) for more info.



### Current limitations (at the time of writing)

Worth keeping in mind the limitation (from the official [faq](https://mybinder.readthedocs.io/en/latest/faq.html#user-memory)):

> **How much memory am I given when using Binder?**
> 
> If you or another Binder user clicks on a Binder link, the mybinder.org deployment will run the linked repository. While running, users are guaranteed at least 1GB of RAM, with a maximum of 2GB. This means you will always have 1GB, you may occasionally have between 1 and 2GB, and if you go over 2GB your kernel will be restarted.
> 
> **How long will my Binder session last?**
> 
> Binder is meant for interactive and ephemeral interactive coding, meaning that it is ideally suited for relatively short sessions. Binder will automatically shut down user sessions that have more than 10 minutes of inactivity (if you leave your window open, this will be counted as “activity”).
> 
> Binder aims to provide at least 12 hours of session time per user session. Beyond that, we cannot guarantee that the session will remain running.
> 
> **Can I use mybinder.org for a live demo or workshop?**
> 
> For sure! We hope the demo gods are with you. Please do make sure you have a backup plan in case there is a problem with mybinder.org during your workshop or demo. Occasionally, service on mybinder.org can be degraded, usually because the server is getting a lot of attention somewhere on the internet, because we are deploying new versions of software, or the team can’t quickly respond to an outage.

### Awesome!

Absolutely a big **THANK YOU** to the [mybinder community](https://gitter.im/jupyterhub/binder)!
