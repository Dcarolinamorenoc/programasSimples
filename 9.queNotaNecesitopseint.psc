Algoritmo queNotaNecesito
	Definir certamen1, certamen2, laboratorio, certamenes, certamen3 Como Real
	Escribir "Ingrese la nota del primer certamen: "
	leer certamen1
	
	Escribir "Ingrese la nota del segundo certamen: "
	leer certamen2
	
	Escribir "Ingrese la nota de laboratorio: "
	leer laboratorio
	
	certamenes = (certamen1 + certamen2) / 2
	
	certamen3 = (60 - (certamenes * 0.7 + laboratorio * 0.3)) / 0.7
	
	Escribir "La nota que necesita para aprobar el ramo con una nota final de 60 es: ", certamen3
	
	
FinAlgoritmo
