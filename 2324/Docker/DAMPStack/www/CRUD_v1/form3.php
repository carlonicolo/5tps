<?php
//Initializing the session 
session_start();
?>

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
  <footer>
    <p>Author: 5TPS<br>
      <a href="form1.php">Home</a>
    </p>
  </footer>
</body>

</html>

<?php
//Initializing the session 
//session_start();

$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "demoform";


$conn = new mysqli("mysql", $username, $password, $dbname);

// Create connection
//$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// set parameters and execute
$name = $_SESSION['name'];
$email =  $_SESSION['email_address'];
$tel = $_SESSION['mobile_number'];
$city = $_POST['city'];
$state = $_POST['state'];

$stmt = $conn->prepare("INSERT INTO utenti (nome, telefono, city, stato) VALUES (?, ?, ?, ?)");
$stmt->bind_param("ssss", $name, $tel, $city, $state);


$stmt->execute();

echo "New records created successfully";
echo "<br>";

$stmt->close();

$sql = "SELECT id, nome, telefono, city FROM utenti";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  // output data of each row
  while ($row = $result->fetch_assoc()) {
    echo "id: " . $row["id"] . " - Name: " . $row["nome"] . " " . $row["telefono"] . " " . $row["city"] . "<br>";
  }
} else {
  echo "0 results";
}
$conn->close();

?>