<?php
if(!isset($_POST['submit']))
{
//This page should not be accessed directly. Need to submit the form.
  echo "error; you need to submit the form!";
}
// $name = $_POST['name'];
$subject = $_POST['subject'];
$visitor_email = $_POST['email'];
$message = $_POST['message'];

//Validate first
if(empty($subject)||empty($visitor_email))
{
    echo "Subject and Email needed";
    exit;
}

if(IsInjected($visitor_email))
{
    echo "Bad email value!";
    exit;
}
// $name = $_POST['name'];
$subject = $_POST['subject'];
$visitor_email = $_POST['email'];
$message = $_POST['message'];

//Compose the message
$email_from = "cpstngroup52020@gmail.com";

$email_subject = $subject;

$email_body = "You have received a new message from your capstone website".
                          "Here is the message:\n $message".

//Using the mail function to send the email
$to = "cpstngroup52020@gmail.com";

$headers = "From: $email_from \r\n";

$headers .= "Reply-To: $visitor_email \r\n";

mail($to,$email_subject,$email_body,$headers);

//form
function IsInjected($str)
{
  $injections = array('(\n+)',
         '(\r+)',
         '(\t+)',
         '(%0A+)',
         '(%0D+)',
         '(%08+)',
         '(%09+)'
         );

  $inject = join('|', $injections);
  $inject = "/$inject/i";

  if(preg_match($inject,$str))
  {
    return true;
  }
  else
  {
    return false;
  }
}

if(IsInjected($visitor_email))
{
  echo "Bad email value!";
  exit;
}
?>
