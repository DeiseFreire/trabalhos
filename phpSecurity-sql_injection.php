<?php
$db = new PDO('mysql:host127.0.01;dbname=website', 'root');
if (isset($_POST['email'])) {
    $email = $_POST['email'];
    $user = $db->prepare("SELECT * FROM users WHERE email = :email");
    $user->execute([
        'email' => $email,
    ]);
    if ($user->rowCount()) {
        die('Send email');
    }
    ?>
<!DOCTYPE html>
<!--
Fonte da ideia:
PHP security: sql injection. 
Produção de Codecourse.
Publicado pelo canal Codecourse. 
[S. l.], 2015. 1 videoaula (9 mins. 15 segs.). Youtube.
-->
<html lang="en">
    <head>
        <meta charset="UTF-8">
              <title>Redefinir senha</title>
              </head>
              <body>
              <form action="sqlinjection.php" method="post" autocomplete="off">
    <label for="email">
        Email address
        <input type="text" name="email" id="email">
    </label>
    <input type="submit" value="Recuperar">
</form>
</body>
</html>
