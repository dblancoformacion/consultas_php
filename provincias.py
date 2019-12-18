import math
import pymysql
con = pymysql.connect('localhost','root','','provincias')
conn = con.cursor()
conn.execute("SELECT * FROM provincias;")
provincias=conn.fetchall()
# Resultado de la consulta
if 0:
	print(provincias)
# (01) Listado de provincias
if 0:
	for p in provincias:
		print(p[1])
# (02) ¿Cuánto suman 2 y 3?
if 0:
	print(2+3)
# (04) Densidades de población de las provincias
if 0:
	for p in provincias:
		print('{} {}'.format(p[1], round(p[2]/p[3],4) ) )
# (52) Obtén el listado del nombre de las provincias que tiene cada autonomía
if 0:
	for p in provincias:
		print('{} {}'.format(p[0], p[1] ) )
# (03) ¿Cuánto vale la raíz cuadrada de 2?
if 0:
	print(round(math.sqrt(2),6))
# (05) ¿Cuántos caracteres tiene cada nombre de provincia?
if 0:
	for p in provincias:
		print('{} {}'.format(p[1],len(p[1])))
# (07) Provincias con el mismo nombre que su comunidad autónoma
if 0:
	for p in provincias:
		if p[0]==p[1]:
			print(p[1])
# (08) Provincias que contienen el diptongo 'ue'
if 1:
	for p in provincias:
		if p[1].find('ue')>0:
			print(p[1])