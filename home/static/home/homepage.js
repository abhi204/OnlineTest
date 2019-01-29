let htmlAdminLoginForm = document.querySelector("#admin-login-form");
let adminLoginButton = document.querySelector("#admin-login-button");
let adminLoginResponse = null;
async function doAdminLogin() {
    let jsForm = new FormData(htmlAdminLoginForm);
    // Add HTML error display element here

    await fetch(
        "/useraccount/admin-login/",
        {
            body: jsForm,
            method: "post",
        }
    ).then(response => (response.json()))
    .then(data => {adminLoginResponse = data})
    .catch(reason => console.log(reason));

    if(adminLoginResponse.response === "success")
    {
        // Do Something on successful account initialization 
        //(verification still pending)
        window.location = "/dashboard";
    } 
    else if(adminLoginResponse.error)
    {
        //Unable to initialize account
        //Display error message appropriately
        window.alert(adminLoginResponse.error);
        // error text is available as adminLoginResponse.errors.{error}.toString()
    }
    else
    {
        //unknown errors here
        window.alert("Unknown Error Occured! (Please try again.)");
    }
}

adminLoginButton.addEventListener("click",doAdminLogin);