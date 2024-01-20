<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Form3 demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
  </head>
  <body>
    <h1>Form3</h1>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
  </body>
</html>

<?php 
    //Initializing the session 
    session_start();

    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "demoform";

    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);
    // Check connection
    if ($conn->connect_error) {
      die("Connection failed: " . $conn->connect_error);
    }

    $stmt = $conn->prepare("INSERT INTO utenti (nome, telefono, city, stato) VALUES (?, ?, ?, ?)");
    $stmt->bind_param("ssss", $name, $tel, $city, $state);

    // set parameters and execute
    $name = $_SESSION['name']; 
    $email =  $_SESSION['email_address'];
    $tel = $_SESSION['mobile_number'];  
    $city = $_POST['city'];
    $state = $_POST['state'];
    $stmt->execute();

    echo "New records created successfully";

    $stmt->close();
    $conn->close();

?>