---
title: Tools
permalink: /tools/
layout: collection
category: tools
---

# Tools Documentation

This section contains documentation for all tools available in the makerspace.

## Tool Categories

### Woodworking Tools
{% for tool in site.tools %}
  {% if tool.category == "woodworking" %}
- [{{ tool.title }}]({{ tool.url }}) - {{ tool.description }}
  {% endif %}
{% endfor %}

### Metalworking Tools
{% for tool in site.tools %}
  {% if tool.category == "metalworking" %}
- [{{ tool.title }}]({{ tool.url }}) - {{ tool.description }}
  {% endif %}
{% endfor %}

### Electronics Tools
{% for tool in site.tools %}
  {% if tool.category == "electronics" %}
- [{{ tool.title }}]({{ tool.url }}) - {{ tool.description }}
  {% endif %}
{% endfor %}

### General Tools
{% for tool in site.tools %}
  {% if tool.category == "general" %}
- [{{ tool.title }}]({{ tool.url }}) - {{ tool.description }}
  {% endif %}
{% endfor %}

## All Tools
{% for tool in site.tools %}
- [{{ tool.title }}]({{ tool.url }}) - {{ tool.description }}
{% endfor %} 