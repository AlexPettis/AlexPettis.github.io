<?php
// Enable error reporting for debugging
error_reporting(E_ALL);
ini_set('display_errors', 1);

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect form data
    $name = strip_tags(trim($_POST["name"]));
    $email = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);
    $message = trim($_POST["message"]);

    // Check that all fields are filled out and email is valid
    if (empty($name) || !filter_var($email, FILTER_VALIDATE_EMAIL) || empty($message)) {
        // Return a 400 error if any field is missing or invalid
        http_response_code(400);
        echo "Please complete the form and try again.";
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

    // Send the email
    if (mail($recipient, $subject, $email_content, $email_headers)) {
        // Redirect to the Thank You page
        header("Location: thank_you.html"); // Corrected the redirection file
        exit;
    } else {
        // Log error to help with debugging
        file_put_contents('php_error.log', "Mail failed: $email_content\n", FILE_APPEND);

        // Failure message
        http_response_code(500);
        echo "Oops! Something went wrong, and we couldn't send your message.";
    }
} else {
    // Return 403 if not a POST request
    http_response_code(403);
    echo "There was a problem with your submission, please try again.";
}
?>
