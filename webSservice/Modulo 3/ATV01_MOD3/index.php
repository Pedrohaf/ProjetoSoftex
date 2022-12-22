<!DOCTYPE html>
<!--
Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
Click nbfs://nbhost/SystemFileSystem/Templates/Project/PHP/PHPProject.php to edit this template
-->
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        <h1> Livros encontrados no estoque:</h1>
        <?php
            require_once 'Livro.php';
            $L1 = new Livro;
            $L1->autor = "Pedro";
            $L1->nome = "Pedro Dev";
            $L1->isbn = "9783161484100";
            
            echo "Nome: ".$L1->nome."->"." Autot: ".$L1->autor."->"." Codigo: ".$L1->isbn
        ?>
    </body>
</html>
