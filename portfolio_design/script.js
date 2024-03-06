function sendMail(){
    const parameters= {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        message: document.getElementById("message").value,
    };

    const serviceID = "service_j9wj0vc";
    const templateID = "template_i1noojb";
    
    //to send the email and clear the  input fields
    emailjs.send(serviceID, templateID, parameters).then((res) =>{
        document.getElementById("name").value = "";
        document.getElementById("email").value = "";
        document.getElementById("message").value = "";
        console.log(res);
    
        alert("Your message has been sent successfully!");
    })
    //catch error
    .catch((err) => console.log(err));
};
  