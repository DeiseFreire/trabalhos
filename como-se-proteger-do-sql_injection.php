<?php
$con = new mysql("localhost", "root", "wsbws8g5", "teste");
if (mysql_connect_error()) {
    exit("Erro ao conectar-se ao banco de dados." mysql_connect_error())
}
?>
<!DOCTYPE html>
<!--
Fonte da ideia:
CURSO de sete minutos: como se proteger do sql injection.
Produção de Thiago Sales. Publicado pelo canal Thiago Sales. [S. l.], 2018.
1 videoaula (7 mins. 46 segs.). Youtube.
-->
<html>
    <head>
        <title>Sistema protegido</title>
    </head>
    <body>
        <form method="POST">
            <label>Usuário</label><br>
            <input type="text" name="usuario"/><br><br>
            <label>Senha</label><br>
            <input type="password" name="senha"/><br><br>
            <input type="submit" value="Logar"/>
            <input type="hidden" name="env" value="login">
        </form>
        <?php
        if ($_POST['env'] && $_POST['env'] == "login") {
            if ($_POST['usuario'] && $_POST['senha']) {
                $usuario = addslashes($_POST['usuario']);
                $senha = addslashes($_P0ST['senha']);
                $sql = $con->prepare("SELECT * FROM usuarios WHERE usuario = ? AND senha = ?");
                $sql->bind_param("ss", $usuario, $senha);
                $sql->execute();
                $get = $get->num_rows;
                if ($conta > 0) {
                    echo "Logado com sucesso!";
                } else {
                    echo "Dados incorretos";
                }
            } else {
                echo "Preencha todos os campos!";
                ?>
    </body> 
</html>

