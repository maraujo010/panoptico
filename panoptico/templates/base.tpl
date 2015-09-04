{% load staticfiles %}		
<!DOCTYPE html>
<html lang="pt">
	<head>		
		<meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /> 
		<meta name="description" content="Panóptico" />
		<meta name="author" content="papalagui010" />
		<title>Panóptico - Observatório</title>				
		<link href="{% static "css/base.css" %}" rel="stylesheet" type="text/css" />
		{%  block  cssFiles  %}{%  endblock  %}		
		{%  block  jsFiles  %}{%  endblock  %}
		<script type="text/javascript" src="{% static "js/jquery-1.11.1.js" %}"></script>																						
	</head>	
	<body>
		<script type="text/javascript">
			$( document ).ready(function() {
				{% block jqueryReadyFunction %}
				{%  endblock  %}		
			});
		</script>
	<div id="imgPreloader">
		<img src="{% static "img/mainMenu_mapa_hover.png" %}" />
		<img src="{% static "img/mainMenu_blog_hover.png" %}" />
		<img src="{% static "img/mainMenu_android_hover.png" %}" />
		<img src="{% static "img/mainMenu_estatisticas_hover.png" %}" />
	</div>
	<div id="mainContainer">
		<div id="innerContainer">		
			<div id="leftSide">
				<div id="loginMenu">													
					{% if user.is_authenticated %}
						<ul>
							<li id="userIcon" {{ menu0Se1ect2 }}><a href="/registar"><span>{{ user.username }}</span></a><img src="{% static "img/dot.png" %}"/></li>
							<li {{ menu0Se1ect1 }}><a href="/logout"><span>LOGOUT</span></a></li>						
						</ul>
					{% else %}
						<ul>
							<li {{ menu0Se1ect2 }}><a href="/registar"><span>CRIAR CONTA</span></a><img src="{% static "img/dot.png" %}"/></li>
							<li {{ menu0Se1ect1 }}><a href="/login"><span>LOGIN</span></a></li>						
						</ul>					
					{% endif %}
					
				</div>	
				<div id="logo">
					<a href="/"><img src="{% static "img/logo.png" %}" alt="Observatório da Videovigilância em Portugal"/></a>
					<h1>Observatório da Videovigilância em Portugal</h1>														
				</div>	
				<div id="mainMenu">
					<ul>
						<li>
							<a  class="mainMenuMapa {{ menu1Se1ect1 }}" href="/"><span>MAPA</span></a>
						</li>
						<li>
							<a  class="mainMenuBlog {{ menu1Se1ect2 }}" href="/blog"><span>BLOG</span></a>
						</li>
						<li>
							<a class="mainMenuApp {{ menu1Se1ect3 }}" href="/androidApp"><span>ANDROID APP</span></a>
						</li>
						<li>
							<a class="mainMenuEstatisticas {{ menu1Se1ect4 }}" href="/estatisticas"><span>ESTASTISTICAS</span></a>
						</li>				
					</ul>				
				</div>
				<div id="pesquisa">
						<form>												
							<input type="text" name="pesquisa" value="pesquisar..." onfocus="if(this.value=='pesquisar...') this.value='';"/>
							<div id="pesquisa_btn"></div>						
						</form>
				</div>
				<div id="secundaryMenu">
					<ul>
						<li {{ menu2Se1ect1 }}><a href="/sobre"><span>Sobre o Observatório</span></li>						
						<li {{ menu2Se1ect2 }}><a href="/participa"><span>Participa</span></li>
						<li {{ menu2Se1ect3 }}><a href="/apoia"><span>Apoia o projecto</span></a></li>
						<li {{ menu2Se1ect4 }}><a href="/contacto"><span>Contacto</span></a></li>									
					</ul>	
				</div>
				<div id="author">
					<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">
						<img alt="Creative Commons License" src="{% static "img/creativecommons.png" %}" />
					</a>											
				</div>												
			</div>			
			<div id="rightSide">					
				{%  block  content  %}{%  endblock  %}			
			</div>	
		</div>
	</div>							
	</body>
</html>
