{%  extends  "base.tpl"  %}

{% block jqueryReadyFunction %}
	
	/*submit form */

	$('#submitRegistrationForm').click(function(){
	     $( "#registrationForm" ).submit();
	});
{%  endblock  %}		

{%  block  content  %}	
<div id="registrationPage">
	<form class="baseForm" id="registrationForm" action="/registar/" method="post" novalidate>
		{% csrf_token %} 
		<ul>
				<li>					
					<label>Username</label>
 					<div class="baseFormInputText"> 						
 						{{ form.username }}
 					</div>
 				</li>
 				<li>
 					<label>Email</label>
 					<div class="baseFormInputText"> 					
 						{{ form.email }}
 					</div>
 				</li>
 				<li> 				 	
 					<label>Password</label>
 				 	<div class="baseFormInputText"> 				 		
 				 		{{ form.password }}
 				 	</div>
 				</li>
 				<li> 				 	
 					<label>Confirma a password</label>
 				 	<div class="baseFormInputText"> 				 		
 				 		{{ form.confirm_password }}
 				 	</div>
 				</li>
		</ul>
		{% if form.errors %}
			{% if 'email' in form.errors.keys %}
				{{ form.errors.email }}
			{% elif 'password' in form.errors.keys %}
				{{ form.errors.password }}
			{% endif %}	
		{% elif failedLogin %}			
			<span class="submitFormError">Email ou password incorrecta</span>
		{% endif %}
		<div class="baseFormSubmit_btn">
			<a id="submitRegistrationForm"><span>Criar conta</span></a>
		</div>
	</form>		
	<div id="loginPageMenu">
		<ul>
			<li><a href="/registar"><span>Politica de privacidade</span></a></li>			
		</ul>
	</div>	
</div>		
{%  endblock  %}