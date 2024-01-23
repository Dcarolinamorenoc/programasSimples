Algoritmo huevosaLaCopa
	Definir TH, TE, M, P, C, K Como Real
    Definir dividendo, divisor, resultado, resultado2, seg, minutos Como Real
	
    Escribir "Temperatura original del huevo"
    Leer TH
	
    TE = 100
    M = 47
    P = 1.638
    C = 3.7
    K = 0.0054
	
    dividendo = (M^(2/3)) * (C * ((P^(1/3))))
    divisor = (K *(Pi^2)) *(((4 * Pi)) / 3)^(2/3)
    resultado = dividendo / divisor
	
    resultado2 = ln(0.76 * ((TH - TE) / (70 - TE)))
	
    seg = resultado * resultado2
    minutos = redon(seg / 60)
	
    Escribir "El tiempo máximo para prepararlo a la copa son", redon(seg), "segundos"
    Escribir "El tiempo máximo para prepararlo a la copa son", minutos, "minutos"
FinAlgoritmo
