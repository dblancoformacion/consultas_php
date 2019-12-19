import math
import pymysql
if 1: # Acceso a la base de datos de provincias
	con = pymysql.connect('localhost','root','','provincias')
	conn = con.cursor(pymysql.cursors.DictCursor)
	conn.execute("SELECT * FROM provincias;")
	provincias=conn.fetchall()
if 0: # Resultado de la consulta
	print(provincias)
if 0: # (01) Listado de provincias
	for p in provincias:
		print(p['provincia'])
if 0: # (02) ¿Cuánto suman 2 y 3?
	print(2+3)
if 0: # (04) Densidades de población de las provincias
	for p in provincias:
		print('{} {}'.format(p['provincia'], round(p[2]/p[3],4) ) )
if 0: # (52) Obtén el listado del nombre de las provincias que tiene cada autonomía
	for p in provincias:
		print('{} {}'.format(p['autonomia'], p['provincia'] ) )
if 0: # (03) ¿Cuánto vale la raíz cuadrada de 2?
	print(round(math.sqrt(2),6))
if 0: # (05) ¿Cuántos caracteres tiene cada nombre de provincia?
	for p in provincias:
		print('{} {}'.format(p['provincia'],len(p['provincia'])))
if 0: # (07) Provincias con el mismo nombre que su comunidad autónoma
	for p in provincias:
		if p['autonomia']==p['provincia']:
			print(p['provincia'])
if 0: # (08) Provincias que contienen el diptongo 'ue'
	for p in provincias:
		if p['provincia'].find('ue')>0:
			print(p['provincia'])
if 0: # (09) Provincias que empiezan por A
	for p in provincias:
		if p['provincia'][0]=='A' or p['provincia'][0]=='Á':
			print(p['provincia'])
if 0: # (17) ¿Qué provincias están en autonomías con nombre compuesto?
	for p in provincias:
		if p['autonomia'].find(' ')>0:
			print(p['provincia'])
if 0: # '18'=>"¿Qué provincias tienen nombre compuesto?",
	for p in provincias:
		if p['provincia'].find(' ')>0:
			print(p['provincia'])
if 0: # '19'=>"¿Qué provincias tienen nombre simple?",
	for p in provincias:
		if p['provincia'].find(' ')<0:
			print(p['provincia'])
if 0: # '51'=>"Muestra las provincias de Galicia, indicando si es Grande, Mediana o Pequeña en función ",
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
if 0: # '10'=>"Autonomías terminadas en 'ana'",
	autonomias={}
	for p in provincias:
		if p['autonomia'].find('ana')==len(p['autonomia'])-3:
			autonomias[p['autonomia']]=1
	for a in autonomias:
		print(a)
if 0: # '11'=>"¿Cuántos caracteres tiene cada nombre de comunidad autónoma? Ordena el resultado por el ",
	autonomias={}
	for p in provincias:
		autonomias[p['autonomia']]=len(p['autonomia'])
	for a in autonomias:
		print('{} {}'.format(a,autonomias[a]))
if 0: # '12'=>"¿Qué autonomías tienen nombre compuesto? Ordena el resultado alfabéticamente en orden ",
	autonomias={}
	for p in provincias:
		if(p['autonomia'].find(' ')>0):
			autonomias[p['autonomia']]=1
	for a in autonomias:
		print(a)
if 0: # '13'=>"¿Qué autonomías tienen nombre simple? Ordena el resultado alfabéticamente en orden ",
	autonomias={}
	for p in provincias:
		if(p['autonomia'].find(' ')<0):
			autonomias[p['autonomia']]=1
	for a in sorted(autonomias.keys()):
		print(a)
if 0: # '14'=>"¿Qué autonomías tienen provincias con nombre compuesto? Ordenar el resultado ",
	autonomias={}
	for p in provincias:
		if(p['provincia'].find(' ')>0):
			autonomias[p['autonomia']]=1
	for a in sorted(autonomias.keys()):
		print(a)
if 0: # '15'=>"Autonomías que comiencen por 'can' ordenadas alfabéticamente",
	autonomias={}
	for p in provincias:
		if(p['autonomia'].find('Can')==0):
			autonomias[p['autonomia']]=1
	for a in sorted(autonomias.keys()):
		print(a)
if 0: # '16'=>"¿Qué autonomías tienen provincias de más de un millón de habitantes? Ordénalas ",
	autonomias={}
	for p in provincias:
		if(p['poblacion']>1e6):
			autonomias[p['autonomia']]=1
	for a in sorted(autonomias.keys()):
		print(a)
if 0: # '21'=>"Población del país",
	poblacion=0
	for p in provincias:
		poblacion+=p['poblacion']
	print(poblacion)
if 0: # '22'=>"Superficie del país",
	superficie=0
	for p in provincias:
		superficie+=p['superficie']
	print(superficie)
if 0: # '23'=>"¿Cuántas provincias hay en la tabla?",
	print(len(provincias))
if 0: # '24'=>"En un listado alfabético, ¿qué provincia estaría la primera?",
	ps=[]
	for p in provincias:
		ps.append(p['provincia'])
	ps.sort()
	print(ps)
if 0: # '25'=>"¿Qué comunidades autónomas contienen el nombre de una de sus provincias?",
	autonomias={}
	for p in provincias:
		if p['autonomia'].find(p['provincia'])>0:
			autonomias[p['autonomia']]=1
	for a in autonomias:
		print(a)
if 0: # '26'=>"¿Qué provincias tienen un nombre más largo que el de su autonomía?",
	for p in provincias:
		if len(p['provincia'])>len(p['autonomia']):
			print(p['provincia'])
if 0: # '27'=>"¿Cuántas comunidades autónomas hay?",
	autonomias={}
	for p in provincias:
		autonomias[p['autonomia']]=1
	print(len(autonomias))
if 0: # '29'=>"¿Cuánto mide el nombre de autonomía más corto?",
	l=10
	for p in provincias:
		if len(p['provincia'])<l:
			l=len(p['provincia'])
	print(l)
if 0: # '30'=>"¿Cuánto mide el nombre de provincia más largo?",
	l=0
	for p in provincias:
		if len(p['provincia'])>l:
			l=len(p['provincia'])
	print(l)
if 0: # '28'=>"Población media de las provincias entre 2 y 3 millones de habitantes sin decimales",
	poblaciones=[]
	for p in provincias:
		if p['poblacion']>=2e6 and p['poblacion']<=3e6:
			poblaciones.append(p['poblacion'])
	print(round(sum(poblaciones)/len(poblaciones)))
if 0: # '53'=>"Obtén el listado de autonomías: una línea por autonomía, junto al listado de sus provincias",
	autonomias={}
	v=''
	for p in provincias:
		autonomias[p['autonomia']]=1
	for a in autonomias:
		print('{} {}'.format(a,v))
if 0: # '31'=>"Provincia más poblada",
	pob=0
	for p in provincias:
		if p['poblacion']>pob:
			pob=p['poblacion']
	for p in provincias:
		if p['poblacion']==pob:
			print(p['provincia'])
if 0: # '32'=>"Provincia más poblada de las inferiores a 1 millón de habitantes",
	pob=0
	for p in provincias:
		if p['poblacion']>pob and p['poblacion']<1e6:
			pob=p['poblacion']
	for p in provincias:
		if p['poblacion']==pob and p['poblacion']<1e6:
			print(p['provincia'])
if 0: # '34'=>"Provincia menos poblada de las superiores al millón de habitantes",
	pob=5e6
	for p in provincias:
		if p['poblacion']<pob and p['poblacion']>1e6:
			pob=p['poblacion']
	for p in provincias:
		if p['poblacion']==pob and p['poblacion']>1e6:
			print(p['provincia'])
if 0: # '35'=>"¿En qué autonomía está la provincia más extensa?",
	sup=0
	for p in provincias:
		if sup<p['superficie']:
			sup=p['superficie']
	for p in provincias:
		if sup==p['superficie']:
			print(p['autonomia'])
if 0: # '36'=>"¿Qué provincias tienen una población por encima de la media nacional?",
	media=0
	for p in  provincias:
		media+=p['poblacion']
	media/=len(provincias)
	for p in provincias:
		if p['poblacion']>media:
			print(p['provincia'])
if 0: # '37'=>"Densidad de población del país",
	pob=0
	sup=0
	for p in provincias:
		pob+=p['poblacion']
		sup+=p['superficie']
	print(round(pob/sup,4))
if 0: # '38'=>"¿Cuántas provincias tiene cada comunidad autónoma?",
	autonomias={}
	for p in provincias:
		try: autonomias[p['autonomia']]
		except:	autonomias[p['autonomia']]=0
		autonomias[p['autonomia']]+=1
	for a in autonomias:
		print('{} {}'.format(a,autonomias[a]))
if 1: # '39'=>"Listado del número de provincias por autonomía ordenadas de más a menos provincias y ",
	autonomias={}
	for p in provincias:
		try: autonomias[p['autonomia']]
		except:	autonomias[p['autonomia']]=0
		autonomias[p['autonomia']]+=1
	for a in sorted(autonomias.items(),key =
             lambda kv:(kv[1], kv[0]),reverse=True):
		print(a)
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