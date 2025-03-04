---
title: Spaces
permalink: /spaces/
layout: collection
category: spaces
---

# Makerspace Areas

This section contains information about all areas in the makerspace.

## Workshop Areas
{% for space in site.spaces %}
  {% if space.type == "workshop" %}
- [{{ space.title }}]({{ space.url }}) - {{ space.description }}
  {% endif %}
{% endfor %}

## Specialized Areas
{% for space in site.spaces %}
  {% if space.type == "specialized" %}
- [{{ space.title }}]({{ space.url }}) - {{ space.description }}
  {% endif %}
{% endfor %}

## Common Areas
{% for space in site.spaces %}
  {% if space.type == "common" %}
- [{{ space.title }}]({{ space.url }}) - {{ space.description }}
  {% endif %}
{% endfor %}

## All Spaces
{% for space in site.spaces %}
- [{{ space.title }}]({{ space.url }}) - {{ space.description }}
{% endfor %}

## Space Map
{% include spaces/spaces.html %} 