<?php
/**
 * Created by PhpStorm.
 * User: arodrigues
 * Date: 6/6/18
 * Time: 3:13 PM
 */


if(isset($_POST['lumini']) && isset($_POST['lumifim']) && isset($_POST['lumifx']) && isset($_POST['regaxhoras']) && isset($_POST['regaifhumambiente']) &&
    isset($_POST['regaifhumsolo']) && isset($_POST['regasegundos']) && isset($_POST['aquecimento'])){

    $data = $_POST['lumini'] . ',' . $_POST['lumifim'] .',' . $_POST['lumifx'] . ',' . $_POST['regaxhoras'] . ',' .
        $_POST['regaifhumambiente'] . ',' . $_POST['regaifhumsolo']. ',' . $_POST['regasegundos']. ',' . $_POST['aquecimento'] . "\n";
    $ret = file_put_contents('config.txt', $data,  LOCK_EX);
    if($ret === false) {
        die('Erro na escrita do ficheiro.');
    }
    else {
        echo "Configuracao guardada com sucesso.";
    }
}
else {
    die('Sem dados para processar.');
}
?>