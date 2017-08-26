<?php
session_start();
system("python cliente.py 2");
$_SESSION["estado"]="<a href='/LASFILES/output.las'  class='btn btn-primary btn-lg' download='output.las'>Descargar Archivo</a><br>";
header("Location: /index.php");
  ?>
