<?php
//header('Content-Type: application/json');
header('Content-type:application/json;charset=utf-8');
if(1){	// conexión a la base de datos y generación del array $provincias
	$conn = new mysqli('localhost','root','','provincias');
	$conn->query("SET NAMES utf8;");
	$provincias=$conn->query("
		SELECT * FROM provincias;
	")->fetch_all(MYSQLI_ASSOC);
	echo json_encode($provincias);
}