function login(){
    var email = document.getElementById("floatingInput");
    var pass = document.getElementById("floatingPassword");
    if(email.value == "user" && pass.value == "user"){
      alert("Success");
      window.location = "registration.html";
    }
    else if (email.value == "admin" && pass.value == "admin"){
      window.location = "Approval.html";
      alert("Admin");
    }
    else{
      alert("Unknown User");
    }
     
  }