// This is a javascript script for checking the user's input

let u_name = document.querySelector("u_name").innerdata
let password = document.querySelector("password").innerdata
let c_password = document.querySelector("c_password").innerdata
let pincode  = document.querySelector("pincode").innerdata
let address = document.querySelector("address").innerdata
let email = document.querySelector("email").innerdata
let l_name = document.querySelector("l_name").innerdata
let f_name = document.querySelector("f_name").innerdata
let submit = document.querySelector(".sign-btn")

submit.addEventListener('click', function (){

    if (password.value != c_password.value)
    {
        alert("The password you entered was not equal to the confirm password - Try Again")
        password = ''
        c_password = ''
    }
    else
    {
        document.write("Your Login is getting procced")
    }

    return 0;
})