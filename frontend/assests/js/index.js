
// const form = document.getElementById("form");
// const loginButton = document.getElementById("login-form-submit");
// const email_error = document.getElementById('error-txt');


// loginButton.addEventListener("click", (e) => {
//     e.preventDefault();
//     const useremail = form.email.value;
//     const password = form.pass.value;

   
//     if (useremail.length< 9){  
//         useremail.style.border = "1px solid blue";
//         //email_error.style.display = "block";
//         return false;  
//        }else if(password.length<6){  
//        alert("Password must be at least 6 characters long.");  
//          return false;  
//              }  
// })
const email = document.getElementById("email");
const password = document.getElementById("password");
const emailError = document.getElementById("email-error");
const passwordError = document.getElementById("password-error");
const submitBtn = document.querySelector(".login-btn");

email.addEventListener("keyup", () => {
    if (email.value == "") {
      emailError.style.display = "block";
      email.style.border = "1px solid red"
    } else {
      emailError.style.display = "none";
    }
  });

  password.addEventListener("keyup", () => {
    if (password.value == "") {
      passwordError.style.display = "block";
      password.style.border = "1px solid red"
    } else {
      passwordError.style.display = "none";
    }
  });


  submitBtn.addEventListener("click", () => {
    //   e.preventDefault();
    if (email.value == "") {
      emailError.style.display = "block";
    }
    if (password.value == "") {
      passwordError.style.display = "block";
    }
    else{
        emailError.style.display = 'none';
        passwordError.style.display = "none";
        let cred = {
            userName: `${email.value}`,
            password: `${password.value}`
        }
  
        console.log(cred);
  
    }
  });
  