---
layout: default
title: Slides
---

# Training Presentations

{% assign presentations = site.slides  %}
{% for presentation in presentations %}
* [{{ presentation.title }}]
{% endfor %}