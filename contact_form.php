<?php
// Enable error reporting for debugging
error_reporting(E_ALL);
ini_set('display_errors', 1);

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect form data
    $name = strip_tags(trim($_POST["name"]));
    $email = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);
    $message = trim($_POST["message"]);

    // Validate form inputs
    if (empty($name) || !filter_var($email, FILTER_VALIDATE_EMAIL) || empty($message)) {
        // Return a 400 error if any field is missing or invalid
        http_response_code(400);
        echo "Please complete the form with valid information and try again.";
        exit;
    }

    // Set the recipient email address
    $recipient = "alexpettis@icloud.com"; // Replace with your email

    // Set the email subject
    $subject = "New Contact from $name";

    // Build the email content
    $email_content = "Name: $name\n";
    $email_content .= "Email: $email\n\n";
    $email_content .= "Message:\n$message\n";

    // Build the email headers
    $email_headers = "From: $name <$email>";

    // Try to send the email
    if (mail($recipient, $subject, $email_content, $email_headers)) {
        // Redirect to the Thank You page after email is sent successfully
        header("Location: thank_you.html");
        exit;
    } else {
        // Display an error message if the email fails to send
        http_response_code(500);
        echo "Oops! Something went wrong, and we couldn't send your message. Please try again later.";
        exit;
    }
} else {
    // Return 403 if the request is not a POST request
    http_response_code(403);
    echo "There was a problem with your submission. Please try again.";
}
?>
