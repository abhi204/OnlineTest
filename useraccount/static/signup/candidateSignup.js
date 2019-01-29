let htmlSignupForm = document.querySelector("#signup-form");
let signUpButton = document.querySelector("#signup-button");
let signupResponse = null;
async function doSignUp() {
    let jsForm = new FormData(htmlSignupForm);
    // Add HTML error display element here

    var elem = document.getElementById('loader');
    elem.style.display = 'block';
    await fetch(
        "/useraccount/create/candidate",
        {
            body: jsForm,
            method: "post",
        }
    ).then(response => (response.json()))
    .then(data => {signupResponse = data})
    .catch(reason => console.log(reason));

    if(signupResponse.response === "success")
    {
        // Do Something on successful account initialization 
        //(verification still pending)
        elem.style.display = 'none';
        //window.alert("Thank You For Registering. \n Please verify your specified email account and then login.");
        window.location = "/useraccount/success";
    }
    else if(signupResponse.response === "exists")
    {
        window.alert("User already exists, Please try again.");
    }
    else if(signupResponse.response === "error")
    {
        //Unable to initialize account
        //Display error message appropriately
        window.alert("Please check your details. And try again.");
        // error text is available as signupResponse.errors.{error}.toString()
    }
    else
    {
        //unknown errors here
        window.alert("Unknown Error Occured! (Please try again.)");
    }
}

signUpButton.addEventListener("click",doSignUp);