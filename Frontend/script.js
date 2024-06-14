
function SendMail() {
    var params = {
        from_name: document.getElementById("fname").value,
        lastname: document.getElementById("lname").value,
        email: document.getElementById("email").value,
        province: document.getElementById("province").value,
        message: document.getElementById("message").value
    };

    emailjs.send("service_po7gwf9","template_qhguudl", params).then(alert("Email Sent!"));

}
