// This is a javascript script for checking the user's input


function check()
{    
    let u_name = document.querySelector("u_name").innerdata
    let password = document.querySelector("password").innerdata
    let c_password = document.querySelector("c_password").innerdata
    let pincode  = document.querySelector("pincode").innerdata
    let address = document.querySelector("address").innerdata
    let email = document.querySelector("email").innerdata
    let l_name = document.querySelector("l_name").innerdata
    let f_name = document.querySelector("f_name").innerdata

    check_pass(password, c_password)
}

function check_pass(password, c_password)
{
    if (password != c_password)
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
}