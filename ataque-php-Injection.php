<!DOCTYPE html>
<!--
Fonte da ideia:
AULA 003 - Segurança contra ataque PHP Injection.
Produção de Carlos Ferreira.
Publicado pelo canal EspecializaTi. [S. l.], 2014. 1 videoaula (4 mins. 01 segs.). 
Youtube.
-->
<?php
session_start();
if (!isset($_SESSION['login'])) {
    header("Location: index.php");
}
require_once 'config/config.php';
?>
<html>
    <head>
        <title>Um projeto vunerável</titlte>
        <!--boostrap-->
        <link href ="style/bootstrap.css" rel="stylesheet">
        <link href+"style/bootstrap.min.css" rel="stylesheet">
        <link href="style/style.css" rel="stylesheet">
        </head>
        <body>
            <nav class="navbar navbar-default" role="navigation">
                <div class="container">
                    <div class=navbar-header">
                        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar
                                <span class="sr-only">Toggle navigation</span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar></span>
                                  </button>
                                  <a class src="img/logo.png" alt="Vunerabilidade" class='img-logo'>
                                </a>
                                </div>
                                <div class="collapse navbar-collapse" id="bs-example-navbar-collapase-1">
                                    <ul class="nav navbar-nav scroll">
                                        <li>
                                            <a href="?pag=home.php">Listar</a>
                                        </li>
                                        <li>
                                            <a href="pag=cadastrar.php">Cadastrar</a>
                                        </li>
                                        <li>
                                            <a href="?pag=sobre.php">Sobre</a>
                                        </li>
                                    </ul>
                                </div>
                                </div>
                                </nav>
                                <div class="container">
                                    <?php
                                    if (!$_GET) {
                                        if (file_exists("{$_GET['pag']}"))
                                            include "{$_GET['pag']}";
                                        else
                                            echo 'A página não existe.';
                                    } else {
                                        include "{$_GET['pag']}";
                                    }
                                    ?>
                                </div>
                                <footer>
                                    <p>Deise Freire</p>
                                </footer>
                                </body>
                                </html>
