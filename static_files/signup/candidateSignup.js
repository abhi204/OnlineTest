let htmlSignupForm = document.querySelector("#signup-form");
let signUpButton = document.querySelector("#signup-button");
let signupResponse = null;
async function doSignUp() {
    let jsForm = new FormData(htmlSignupForm);
    // Add HTML error display element here

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
        window.alert("SUCCESS!!!");
        window.location = "/";
    } 
    else if(signupResponse.response === "error")
    {
        //Unable to initialize account
        //Display error message appropriately
        window.alert(signupResponse.errors);
        // error text is available as signupResponse.errors.{error}.toString()
    }
    else
    {
        //unknown errors here
        window.alert("Unknown Error Occured! (Please try again.)");
    }
}

signUpButton.addEventListener("click",doSignUp);