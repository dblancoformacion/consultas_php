<!doctype html>
<html>
<head>
<style>
#ini>div>.primero{
	background-color:blue;
}
</style>
<script>
window.onload=hora;
function hora(){
	f=new Date();
	document.getElementById('hora').innerHTML=
		+("0" + f.getHours()).slice(-2)
		+':'+("0" + f.getMinutes()).slice(-2);
}
function test(id){
	
	console.log(document.getElementById(id)['src']);
	console.log(document.querySelector('a>#prueba')['href']);
	console.log(document.querySelectorAll('a')[4]['href']);
	console.log(document.querySelector('#ini>div>.primero').innerHTML);
}
</script>
</head>
<body>
<div id="hora"></div>
<div id="ini">
	<a></a><a></a><a></a> ... <a></a>
	<a href="enlace?campo1=dato1&campo2=dato2"><img src="foco_ok.png" 
		id="prueba"
		onclick="test('prueba');return false;"
	></a>
	<div>
		has llegado
		<div class="primero">1</div>
		<div>2</div>
		<div>3</div>
	</div>
</div>
</html>