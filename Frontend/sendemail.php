<?php
// Check if the form was submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect and sanitize input data
    $firstname = filter_input(INPUT_POST, 'firstname', FILTER_SANITIZE_STRING);
    $lastname = filter_input(INPUT_POST, 'lastname', FILTER_SANITIZE_STRING);
    $province = filter_input(INPUT_POST, 'province', FILTER_SANITIZE_STRING);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_STRING);

    // Recipient email address
    $to = 'alicex0609@gmail.com';

    // Subject line for the email
    $subject = 'New Contact Form Submission';

    // Construct the email content
    $email_content = "You have received a new message from the contact form:\n\n";
    $email_content .= "First Name: $firstname\n";
    $email_content .= "Last Name: $lastname\n";
    $email_content .= "Province: $province\n";
    $email_content .= "Message:\n$message\n";

    // Email headers
    $headers = "From: noreply@example.com\n";
    $headers .= "Reply-To: $email";

    // Send the email
    if (mail($to, $subject, $email_content, $headers)) {
        echo 'Thank you for contacting us. We will get back to you soon!';
    } else {
        echo 'Sorry, there was an error sending your message. Please try again later.';
    }
} else {
    // Not a POST request, set a 403 (forbidden) response code.
    http_response_code(403);
    echo "There was a problem with your submission, please try again.";
}
?>
