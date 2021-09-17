---
title: "Calculating Industry Collaborations via GRID"
date: "2020-01-08"
categories: 
  - "data-science"
---

> A new [tutorial](https://api-lab.dimensions.ai/cookbooks/8-organizations/2-Industry-Collaboration.html) demostrating how to extract and visualize data about _industry collaborations_, by combining the Dimensions data with GRID.

Dimensions uses [GRID](https://grid.ac/) (the Global Research Identifiers Database) to unambiguously identify research organizations. GRID includes a wealth of data, for example whether an organization has type 'Education' or 'Industry'. So it's pretty easy to take advantage of these metadata in order to highlight collaboration patterns between a selected university and other organizations from the industry sector.

The [Identifying the Industry Collaborators of an Academic Institution](https://api-lab.dimensions.ai/cookbooks/8-organizations/2-Industry-Collaboration.html) notebook can be adapted so to focus on any research organization: many of us are linked to some university, hence it's quite interesting to explore what are the non-academic organizations related to 

> The [Dimensions API](https://www.dimensions.ai/dimensions-apis/) can be accessed for **free** for [non-commercial research projects.](https://www.dimensions.ai/scientometric-research/)


For example, see below a [Plotly](https://plot.ly/python/) visualization of the industry collaborators for [University of Trento, Italy](https://grid.ac/institutes/grid.11696.39).

[![plotly-chart](/media/static/blog_img/2020-01-08-calculating-industry-collaborations-via-grid.jpg)](/media/static/blog_img/2020-01-08-calculating-industry-collaborations-via-grid.jpg)

