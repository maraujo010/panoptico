{%  extends  "base.tpl"  %}
{% load staticfiles %}	

{%  block  cssFiles  %}
	<link href="{% static "css/mapa.css" %}" rel="stylesheet" type="text/css" />
{%  endblock  %}	

{%  block  jsFiles  %}
	<script src="{% static "js/OpenLayers/OpenLayers.js" %}"></script>
	<script src="/static/js/mapa.js"></script>	
{%  endblock  %}	

{%  block  content  %}

<div id="mapaDiv">	
</div>

<script>
	/*totalHeight = $(document).height();
	$("#mapaDiv").css({'height':(totalHeight +'px')});*/	
	var mapa = new OpenLayers.Map('mapaDiv');	
	initMapa(mapa);
</script> 	

{%  endblock  %}