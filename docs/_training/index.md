---
title: Training
permalink: /training/
layout: default
category: training
---

# Training Documentation

This section contains all training materials and courses available at the makerspace.

## Training Categories

### Safety Training
{% for training in site.training %}
  {% if training.category == "safety" %}
- [{{ training.title }}]({{ training.url }}) - {{ training.duration }} | Level: {{ training.level }}
  {% endif %}
{% endfor %}

### Tool-Specific Training
{% for training in site.training %}
  {% if training.category == "tools" %}
- [{{ training.title }}]({{ training.url }}) - {{ training.duration }} | Level: {{ training.level }}
  {% endif %}
{% endfor %}

### Project-Based Training
{% for training in site.training %}
  {% if training.category == "projects" %}
- [{{ training.title }}]({{ training.url }}) - {{ training.duration }} | Level: {{ training.level }}
  {% endif %}
{% endfor %}

## Training Slides
- [3D Printer Training](/slides/3Dprinting)
- [CNC Training](/slides/cnc)
- [Laser Cutter Training](/slides/laser)
- [Woodshop Safety](/slides/woodshop-safety)

## All Training Courses
{% for training in site.training %}
- [{{ training.title }}]({{ training.url }}) - {{ training.duration }} | Level: {{ training.level }}
{% endfor %} 