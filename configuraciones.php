<?php
session_start();
$lidar = $_POST["lidar"];
$motor = $_POST["motor"];
try{
if ((int)$motor >10) {
  $_SESSION["estado"]="Velocida Máxima superada";
  header("Location: /index.php");
}
}catch (Exception $e) {
    $_SESSION["estado"]="Error al ingresar datos";
    header("Location: /index.php");
}
$archivo = $_POST["archivo"]; 
$nombre_archivo = 'configuraciones.txt';
$contenido = "lidar;".$lidar."\n"."VelocidadMotor;".$motor."\n"."TamanoArchivo;".$archivo."\n";
fopen($nombre_archivo, 'w');

// Asegurarse primero de que el archivo existe y puede escribirse sobre el.
if (is_writable($nombre_archivo)) {

   // En nuestro ejemplo estamos abriendo $nombre_archivo en modo de adicion.
   // El apuntador de archivo se encuentra al final del archivo, asi que
   // alli es donde ira $contenido cuando llamemos fwrite().
   if (!$gestor = fopen($nombre_archivo, 'a')) {
         echo "No se puede abrir el archivo ($nombre_archivo)";
         exit;
   }

   // Escribir $contenido a nuestro arcivo abierto.
   if (fwrite($gestor, $contenido) === FALSE) {
       echo "No se puede escribir al archivo ($nombre_archivo)";
       exit;
   }
   
   echo "&Eacute;xito, se escribi&oacute; ($contenido) al archivo ($nombre_archivo)";
   
   fclose($gestor);

} else {
   echo "No se puede escribir sobre el archivo $nombre_archivo";
}
$_SESSION["estado"]="Archivo Creado";
header("Location: /index.php");
?>