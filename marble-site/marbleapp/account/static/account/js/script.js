const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('containerlogin');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
	document.getElementById("kaydol1").reset();
	
	
});



signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
	
	
});


