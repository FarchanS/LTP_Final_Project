<?php 

require_once("config.php");

if(isset($_POST['login'])){

    $username = filter_input(INPUT_POST, 'username', FILTER_SANITIZE_STRING);
    $password = filter_input(INPUT_POST, 'password', FILTER_SANITIZE_STRING);

    $sql = "SELECT * FROM user WHERE Nama=:username";
    $stmt = $db->prepare($sql);

    $params = array(
        ":username" => $username
    );

    $stmt->execute($params);

    $user = $stmt->fetch(PDO::FETCH_ASSOC);
    
    // jika user terdaftar
    if($user){
        // verifikasi password
        // if(password_verify($password, $user["Pass"])){
        if($password == $user["Pass"])
        {
            echo "yess.. login suksess..";
            echo '<script>alert("yess.. login suksess..")</script>';
        }
        else 
        {
            echo "Login failed"; 
        }
    }
    else
    {
        echo "Incorrect user";
    }
}
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <title>Login</title>
</head>
<body class="bg-light">

<div class="container mt-5">
    <div class="row">
        <div class="col-md-6">

        <!-- <p>&larr; <a href="index.php">Home</a> -->

        <h4>Masuk ke Seluler Shop</h4>
        <!-- <p>Belum punya akun? <a href="register.php">Daftar di sini</a></p> -->

        <form action="" method="POST">
            <div class="form-group">
                <label for="username">Username</label>
                <input class="form-control" type="text" name="username" placeholder="Username" />
            </div>

            <div class="form-group">
                <label for="password">Password</label>
                <input class="form-control" type="password" name="password" placeholder="Password" />
            </div>

            <input type="submit" class="btn btn-success btn-block" name="login" value="Masuk" />

        </form>
            
        </div>

    </div>
</div>
    
</body>
</html>