function validatePassword() {
   let password = document.getElementById("password").value;
   let confirmPassword = document.getElementById("confirm-password").value;
   let errorMessage = document.getElementById("error-message");

   if (password !== confirmPassword) {
       errorMessage.style.display = "block";
       return false;
       
   } else {
       errorMessage.style.display = "none";
       signup(); // Call the signup function after successful validation
       return true;
   }
}

function signup() {
   alert("You have successfully signed up!");
}
