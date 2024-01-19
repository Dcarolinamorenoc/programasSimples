#Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas:

horaactual=int(input("Querido usuario cual es su hora actual: "))
horadespues=int(input("Querido usuario cual es el numero de horas que desea avanzar: "))

nuevahora=(horaactual+horadespues)%24

print(f"La hora después de {horadespues} horas será: {nuevahora}")