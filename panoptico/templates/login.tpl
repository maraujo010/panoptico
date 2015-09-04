{%  extends  "base.tpl"  %}

{% block jqueryReadyFunction %}
	/* password change value */

	var passwordField = $('input[name=password]');
	passwordField.after('<input id="passwordPlaceholder" type="text" value="password..." autocomplete="off" />');
	var passwordPlaceholder = $('#passwordPlaceholder');
	
	var emailField = $('input[name=email]');
    var emailFieldDefault = emailField.val();
	
	passwordPlaceholder.show();
    passwordField.hide();

	passwordPlaceholder.focus(function() {
		passwordPlaceholder.hide();
		passwordField.show();
		passwordField.focus();
    });

	passwordField.blur(function() {
        if(passwordField.val() == '') {
           passwordPlaceholder.show();
           passwordField.hide();
        }
    });

    emailField.focus(function() {
		if(emailField.val() == emailFieldDefault) {
			emailField.val('');
	    }
	});
	
	emailField.blur(function() {
	   if(emailField.val() == '') {
			emailField.val(emailFieldDefault);
	   }
	});
	
	/*submit form */

	$('#submitLogin').click(function(){
	     $( "#loginForm" ).submit();
	});
{%  endblock  %}		

{%  block  content  %}	
<div id="loginPage">
	<div id="loginArea">
		<form class="baseForm" id="loginForm" action="/login/" method="post" novalidate>
			{% csrf_token %} 
			<ul>
 				<li>
 					<div class="baseFormInputText">{{ form.email }}</div>
 				</li>
 				<li> 				 	
 				 	<div class="baseFormInputText">{{ form.password }}</div>
 				</li>
			</ul>
			{% if form.errors %}
				{% if 'email' in form.errors.keys %}
					{{ form.errors.email }}
				{% elif 'password' in form.errors.keys %}
					{{ form.errors.password }}
				{% endif %}	
			{% elif failedLogin %}			
				<span class="submitFormError">{{ failedLogin }}</span>
			{% endif %}
			<div class="baseFormSubmit_btn">
				<a id="submitLogin"><span>Login</span></a>
			</div>
		</form>		
	</div>
	<div id="loginPageMenu">
		<ul>
			<li><a href="/registar"><span>Cria Conta</span></a></li>
			<li><a href="/recuperarpass"><span>Recuperar Password</span></a></li>
		</ul>
	</div>	
</div>		
{%  endblock  %}