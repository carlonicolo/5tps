<?php

// Initialize the session 
session_start();

// Store the submitted data sent 
// via POST method, stored  

// Temporarily in $_POST structure. 
$_SESSION['name'] = $_POST['user_name'];

$_SESSION['email_address']
    = $_POST['user_email_address'];

$_SESSION['mobile_number']
    = $_POST['user_mobile_number'];

?>

<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Form2 demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
</head>

<body>
    <h1>Form2</h1>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
    <!-- Form for other details-->
    <form method="POST" action="form3.php">

        <pre>
        Company/College:  
        <input type="text" name="college_name"> 
    </pre>

        <pre>
        City:  
        <input type="text" name="city"> 
    </pre>

        <pre>
        State:  
        <input type="text" name="state"> 
    </pre>

        <pre>
        You're a:  
        <input type="radio" name="profession"
                value="Student">Student 
          
        <input type="radio" name="profession"
                value="Working Professional"> 
                Working Professional 
    </pre>

        <pre>
        Course:  
        <select name="course"> 
            <option value="DSnA"> 
                Data Structures and Algorithms 
            </option> 
              
            <option value="Gate_test"> 
                GATE Mock Test 
            </option> 
              
            <option value="Mock_interview"> 
                Mock Interviews 
            </option> 
              
            <option value="Machine_learning"> 
                Machine Learning 
            </option> 
        </select> 
    </pre>
        <br>

        <pre>
        <input type="checkbox" 
            name="terms_and_conditions">  
            Terms and Conditions  
    </pre>
        <br>

        <input type="submit" value="Register">

    </form>

</body>

</html>