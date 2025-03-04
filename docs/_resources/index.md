---
title: Resources
permalink: /resources/
layout: collection
category: resources
---

# Resources

This section contains various resources and reference materials for the makerspace.

## Resource Categories

### Guides and Manuals
{% for resource in site.resources %}
  {% if resource.type == "guide" %}
- [{{ resource.title }}]({{ resource.url }}) - Last updated: {{ resource.date }}
  {% endif %}
{% endfor %}

### Templates and Files
{% for resource in site.resources %}
  {% if resource.type == "template" %}
- [{{ resource.title }}]({{ resource.url }}) - Last updated: {{ resource.date }}
  {% endif %}
{% endfor %}

### Video Resources
{% for resource in site.resources %}
  {% if resource.type == "video" %}
- [{{ resource.title }}]({{ resource.url }}) - Last updated: {{ resource.date }}
  {% endif %}
{% endfor %}

## All Resources
{% for resource in site.resources %}
- [{{ resource.title }}]({{ resource.url }}) - Type: {{ resource.type }} | Last updated: {{ resource.date }}
{% endfor %} 