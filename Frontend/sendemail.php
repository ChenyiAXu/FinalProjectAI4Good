<?php
// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect POST data from the form
    $firstName = htmlspecialchars($_POST['firstname']);
    $lastName = htmlspecialchars($_POST['lastname']);
    $email = htmlspecialchars($_POST['email']);
    $province = htmlspecialchars($_POST['province']);
    $message = htmlspecialchars($_POST['message']);

    // Prepare the email content
    $to = 'alicex0609@gmail.com'; // Change this to your email address
    $subject = 'New Message from Website';
    $emailContent = "First Name: $firstName\n";
    $emailContent .= "Last Name: $lastName\n";
    $emailContent .= "Email: $email\n";
    $emailContent .= "Province: $province\n";
    $emailContent .= "Message: $message\n";

    $headers = "From: $email";

    // Send the email
    if (mail($to, $subject, $emailContent, $headers)) {
        echo "Thank you for your message. It has been sent.";
    } else {
        echo "There was an error sending your message. Please try again later.";
    }
} else {
    // Not a POST request
    echo "Error: You must submit the form!";
}
?>
