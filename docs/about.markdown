---
sort: 99
layout: default
title: About
permalink: /about/
---

The Creation Nation Makerspace is a non-profit project of the Brandon Neighbourhood Renewal Corporation.


<ul>
{% for member in site.data.members %}
  <li>
    <a href="https://github.com/{{ member.github }}">
      {{ member.name }}
    </a>
  </li>
{% endfor %}

{% for space in site.spaces %}
  <li>
    <a href="{{space.url}}">
      {{ space.title }}
    </a>
  </li>
{% endfor %}

</ul>