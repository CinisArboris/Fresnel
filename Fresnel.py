def limpiar():
	os.system("cls")
	
def bannerPrimeraZonaFresnel():
	print ("F1 - radio de la primera zona de Fresnel (m)")
	print ("r1 - distancia de la antena al obstáculo (km)")
	print ("r2 - distancia de la antena al obstáculo (km)")
	print ("r  - distancia entre antenas (km)")
	print ("f  - frecuencia de operación del sistema (GHz)")

def primeraZonaFresnel (r1, r2, r, f):
	bannerPrimeraZonaFresnel()
	numerador = r1 * r2
	denominador = r * f
	#print ("ss", (numerador/denominador)**(1/2) )
	return ((((numerador/denominador)**(1/2))*17.32)*0.6)

def welcome(seleccion):	
	print ("Bienvenido :)")
	print ("Ëlija una opcion: ")
	print ("Op 1 - primeraZonaFresnel")
	print ("null")
	print ("null")
	print ("null")
	print ("null")
	seleccion = float(input("Tu seleccion ::: "))
	return seleccion

import os



limpiar()
seleccion = 0

F1 = 1.0
r1 = 1.0
r2 = 1.0
r = 1.0
f = 1.0
	
seleccion = welcome(seleccion)
if (seleccion == 1):
	bannerPrimeraZonaFresnel()
	r1 = float(input("r1 :: "))
	r2 = float(input("r2 :: "))
	r  = float(input("r  :: "))
	f  = float(input("f  :: "))
	F1 = primeraZonaFresnel(r1, r2, r, f)
	F1 = "%.2f" % F1
	#limpiar()
	print ("Primera Zona de Fresnel", F1)
	print (F1, "Es la distancia max, que no debe haber interferencia.")
else:
	print("Ninguna opcion seleccionada, hasta luego :)")
