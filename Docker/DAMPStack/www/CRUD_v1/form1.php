<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Form1 demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="css/style.css">
</head>

<body>
    <h1>Form1</h1>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>

    <form method="POST" action="form2.php">
        <pre>Name: <input type="text"
		name="user_name"> 
	</pre>

        <pre>Email Address: <input type="text"
		name="user_email_address"> 
	</pre>

        <pre>Mobile Number: <input type="number"
		name="user_mobile_number"> 
	</pre>

        <input type="submit" value="Next">
    </form>
    <footer>
    <p class="footer_author">Author: 5TPS<br>
      <a href="form1.php">Home</a>
    </p>
  </footer>

</body>

</html>