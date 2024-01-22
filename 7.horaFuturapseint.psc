Algoritmo horaFutura
	Definir Horactual, horadesp, nuevahora Como Entero
	Escribir "Querido usuario cual es su hora actual: "
	leer Horactual
	
	Escribir "Querido usuario cual es el numero de horas que desea avanzar: "
	Leer horadesp
	
	nuevahora=(horactual+horadesp)%24
	
	Escribir "La nueva hora será: ", nuevahora
	
FinAlgoritmo
