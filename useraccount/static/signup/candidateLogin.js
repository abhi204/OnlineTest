let htmlCandidateLoginForm = document.querySelector("#candidate-login-form");
let candidateLoginButton = document.querySelector("#candidate-login-button");
let candidateLoginResponse = null;

async function doCandidateLogin() {
    let jsForm = new FormData(htmlCandidateLoginForm);
    // Add HTML error display element here

    await fetch(
        "/useraccount/candidate-login/",
        {
            body: jsForm,
            method: "post",
        }
    ).then(response => (response.json()))
    .then(data => {candidateLoginResponse = data})
    .catch(reason => console.log(reason));

    if(candidateLoginResponse.response === "success")
    {
        // Do Something on successful account initialization
        //(verification still pending)
        window.alert("SUCCESS!!!");
        window.location = "/useraccount/courses/";
    }
    else if(candidateLoginResponse.error)
    {
        //Unable to initialize account
        //Display error message appropriately
        window.alert(candidateLoginResponse.error);
        // error text is available as adminLoginResponse.errors.{error}.toString()
    }
    else
    {
        //unknown errors here
        window.alert("Unknown Error Occured! (Please try again.)");
    }
}

candidateLoginButton.addEventListener("click",doCandidateLogin);