let id = (id) => document.getElementById(id);

let classes = (classes) => document.getElementsByClassName(classes);

let Name = id("Name"),
  email = id("email"),
  password = id("password"),
  Password = id("Password"),
  form = id("form"),

  error = classes("error"),
  loginButton = classes("login-btn");

  let engine = (id, serial, message) => {
    if (id.value.trim() === "") {
        error[serial].innerHTML = message;
        id.style.border = "2px solid red";
  } else {
    error[serial].innerHTML = "";
    id.style.border = "2px solid green";
  }
  }

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    engine(Name, 0, "Username cannot be blank");
    engine(email, 1, "Email cannot be blank");
    engine(password, 2, "Password cannot be blank");
    engine(Password,3 , "Password cannot be blank");
  });

  