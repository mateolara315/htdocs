<?php
// Conectando, seleccionando la base de datos
$conn = new mysqli("127.0.0.1", "root", "12345", "fredym"); // conecta al servidor con user, contraseña


// Realizar una consulta MySQL
$query = "SELECT * FROM syrus ORDER BY id DESC LIMIT 1"; // ultimo valor de la tabla llamada datos
$resultado = mysqli_query($conn, $query) or die("Consulta fallida: " . mysqli_error()); // guardo en resultado lo que saqué de query

$fila = mysqli_fetch_row($resultado); // guardo en un array lo que está en resultado, como string

$var = $fila[1]."\n".$fila[2]."\n".$fila[3];

echo $var;
mysqli_close($conn);

?>
