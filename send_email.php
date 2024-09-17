<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect form data
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $howDidYouFindMe = htmlspecialchars($_POST['howDidYouFindMe']);
    $otherText = htmlspecialchars($_POST['otherText']);
    $message = htmlspecialchars($_POST['message']);
    
    // Prepare the email
    $to = "alexpettis@icloud.com"; // Replace with your email
    $subject = "New Contact Form Submission";
    $body = "Name: $name\nEmail: $email\nHow Did You Find Me: $howDidYouFindMe\n";
    
    // Append 'Other' field if applicable
    if ($howDidYouFindMe == "other") {
        $body .= "Other: $otherText\n";
    }

    $body .= "Message:\n$message";

    // Email headers
    $headers = "From: $email";

    // Send email
    if (mail($to, $subject, $body, $headers)) {
        // Redirect to thank you page if mail is successful
        header('Location: thankyou.html');
        exit();
    } else {
        echo "There was a problem sending your email. Please try again later.";
    }
}
?>
