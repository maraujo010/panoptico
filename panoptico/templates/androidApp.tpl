{%  extends  "base.tpl"  %}
{% load staticfiles %}	

{%  block  cssFiles  %}
	<link href="{% static "css/mapa.css" %}" rel="stylesheet" type="text/css" />
{%  endblock  %}	

{%  block  jsFiles  %}
{%  endblock  %}	

{%  block  content  %}
<div class="rightSideTop">
	<img src="{% static "img/androidApp_area.png" %}" />
</div>
<div>
</div>

{%  endblock  %}