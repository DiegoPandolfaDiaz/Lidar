<?php
session_start();
$_SESSION['muestreo']=0;
$_SESSION['las']=1;
system("python cliente.py 0");
header("Location: /index.php");
  ?>