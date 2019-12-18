import math
import pymysql
con = pymysql.connect('localhost','root','','provincias')
conn = con.cursor(pymysql.cursors.DictCursor)
conn.execute("SELECT * FROM provincias;")
provincias=conn.fetchall()
# Resultado de la consulta
if 0:
	print(provincias)
# (01) Listado de provincias
if 0:
	for p in provincias:
		print(p['provincia'])
# (02) ¿Cuánto suman 2 y 3?
if 0:
	print(2+3)
# (04) Densidades de población de las provincias
if 0:
	for p in provincias:
		print('{} {}'.format(p['provincia'], round(p[2]/p[3],4) ) )
# (52) Obtén el listado del nombre de las provincias que tiene cada autonomía
if 0:
	for p in provincias:
		print('{} {}'.format(p['autonomia'], p['provincia'] ) )
# (03) ¿Cuánto vale la raíz cuadrada de 2?
if 0:
	print(round(math.sqrt(2),6))
# (05) ¿Cuántos caracteres tiene cada nombre de provincia?
if 0:
	for p in provincias:
		print('{} {}'.format(p['provincia'],len(p['provincia'])))
# (07) Provincias con el mismo nombre que su comunidad autónoma
if 0:
	for p in provincias:
		if p['autonomia']==p['provincia']:
			print(p['provincia'])
# (08) Provincias que contienen el diptongo 'ue'
if 0:
	for p in provincias:
		if p['provincia'].find('ue')>0:
			print(p['provincia'])
# (09) Provincias que empiezan por A
if 0:
	for p in provincias:
		if p['provincia'][0]=='A' or p['provincia'][0]=='Á':
			print(p['provincia'])
# (17) ¿Qué provincias están en autonomías con nombre compuesto?
if 0:
	for p in provincias:
		if p['autonomia'].find(' ')>0:
			print(p['provincia'])
# '18'=>"¿Qué provincias tienen nombre compuesto?",
if 0:
	for p in provincias:
		if p['provincia'].find(' ')>0:
			print(p['provincia'])
# '19'=>"¿Qué provincias tienen nombre simple?",
if 0:
	for p in provincias:
		if p['provincia'].find(' ')<0:
			print(p['provincia'])
# '51'=>"Muestra las provincias de Galicia, indicando si es Grande, Mediana o Pequeña en función ",
if 0:
	for p in provincias:
		if p['autonomia']=='Galicia':
			if p['poblacion']>1e6:
				r='Grande'
			else:
				if p['poblacion']>5e5:
					r='Mediana'
				else:
					r='Pequeña'
			print('{} {}'.format(p['provincia'],r))
# '10'=>"Autonomías terminadas en 'ana'",
if 0:
	autonomias={}
	for p in provincias:
		if p['autonomia'].find('ana')==len(p['autonomia'])-3:
			autonomias[p['autonomia']]=1
	for a in autonomias:
		print(a)
# '11'=>"¿Cuántos caracteres tiene cada nombre de comunidad autónoma? Ordena el resultado por el ",
if 0:
	autonomias={}
	for p in provincias:
		autonomias[p['autonomia']]=len(p['autonomia'])
	for a in autonomias:
		print('{} {}'.format(a,autonomias[a]))
# '12'=>"¿Qué autonomías tienen nombre compuesto? Ordena el resultado alfabéticamente en orden ",
if 0:
	autonomias={}
	for p in provincias:
		if(p['autonomia'].find(' ')>0):
			autonomias[p['autonomia']]=1
	for a in autonomias:
		print(a)
# '13'=>"¿Qué autonomías tienen nombre simple? Ordena el resultado alfabéticamente en orden ",
if 1:
	autonomias={}
	for p in provincias:
		if(p['autonomia'].find(' ')<0):
			autonomias[p['autonomia']]=1
	for a in sorted(autonomias.keys()):
		print(a)
# '14'=>"¿Qué autonomías tienen provincias con nombre compuesto? Ordenar el resultado ",
# '15'=>"Autonomías que comiencen por 'can' ordenadas alfabéticamente",
# '16'=>"¿Qué autonomías tienen provincias de más de un millón de habitantes? Ordénalas ",
# '21'=>"Población del país",
# '22'=>"Superficie del país",
# '23'=>"¿Cuántas provincias hay en la tabla?",
# '24'=>"En un listado alfabético, ¿qué provincia estaría la primera?",
# '25'=>"¿Qué comunidades autónomas contienen el nombre de una de sus provincias?",
# '26'=>"¿Qué provincias tienen un nombre más largo que el de su autonomía?",
# '27'=>"¿Cuántas comunidades autónomas hay?",
# '29'=>"¿Cuánto mide el nombre de autonomía más corto?",
# '30'=>"¿Cuánto mide el nombre de provincia más largo?",
# '28'=>"Población media de las provincias entre 2 y 3 millones de habitantes sin decimales",
# '53'=>"Obtén el listado de autonomías: una línea por autonomía, junto al listado de sus provincias",
# '31'=>"Provincia más poblada",
# '32'=>"Provincia más poblada de las inferiores a 1 millón de habitantes",
# '34'=>"Provincia menos poblada de las superiores al millón de habitantes",
# '35'=>"¿En qué autonomía está la provincia más extensa?",
# '36'=>"¿Qué provincias tienen una población por encima de la media nacional?",
# '37'=>"Densidad de población del país",
# '38'=>"¿Cuántas provincias tiene cada comunidad autónoma?",
# '39'=>"Listado del número de provincias por autonomía ordenadas de más a menos provincias y ",
# '40'=>"¿Cuántas provincias con nombre compuesto tiene cada comunidad autónoma?",
# '41'=>"Autonomías uniprovinciales",
# '42'=>"¿Qué autonomía tiene 5 provincias?",
# '43'=>"Población de la autonomía más poblada",
# '44'=>"¿Qué porcentaje del total nacional representa Cantabria en población y en superficie?",
# '49'=>"Obtener la provincia más poblada de cada comunidad autónoma, indicando la población de ",
# '47'=>"¿En qué posición del ranking autonómico por población de mayor a menor está Cantabria?",
# '45'=>"Automía más extensa",
# '46'=>"Autonomía con más provincias",
# '48'=>"Provincia más despoblada de la autonomía más poblada",
# '50'=>"Provincia más poblada de la autonomía más despoblada",
# '06'=>"Listado de autonomías",