if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if(!empty($_POST['firstname'])
        && !empty($_POST['lastname'])
        && !empty($_POST['province'])
        && !empty($_POST['message'])
    ) {
        $firstname = $_POST["firstname"];
        $lastname = $_POST["lastname"];
        $province = $_POST["province"];
        $message = $_POST["firstname"];

        $to = 'alicex0609@gmail.com';
        $subject = 'New Contact Form Submission';

        $email_content = "You have received a new message from the contact form:\n\n";
        $email_content .= "First Name: $firstname\n";
        $email_content .= "Last Name: $lastname\n";
        $email_content .= "Province: $province\n";
        $email_content .= "Message:\n$message\n";

      // Email headers
        $headers = "From: noreply@ai4goodlabv3.com\n";
        $headers .= "Reply-To: $firstname <$lastname@example.com>";

        if (mail($to, $subject, $email_content, $headers)) {
        echo 'Thank you for contacting us. We will get back to you soon!';
          } else {
        echo 'Sorry, there was an error sending your message. Please try again later.';
    }



    }
} else{
    http_response_code(403);
    echo "There was a problem with your submission, please try again.";
}