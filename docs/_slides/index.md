---
sort: 1
layout: default
title: Slides
permalink: slides
---
# Training Slides
Training Material for the various tools

<ul>
{% for slide in site.slides %}
  <li>
    <a href="{{ slide.url}}">
      {{ slide.title }}
    </a>
  </li>
{% endfor %}
</ul>