<?php
//header('Content-Type: application/json');
header('Content-type:application/json;charset=utf-8');
if(1){	// conexión a la base de datos
	$conn = new mysqli('localhost','root','','provincias');
	$conn->query("SET NAMES utf8;");
}
if(isset($_GET['id'])){	// incremento de visitas
	$conn->query("
		UPDATE provincias set visitas=visitas+1
			WHERE id=".($_GET['id']*1).";
	");
	echo json_encode([1]);
}
else{	// generación del array $provincias
	$provincias=$conn->query("
		SELECT * FROM provincias;
	")->fetch_all(MYSQLI_ASSOC);
	echo json_encode($provincias);
}