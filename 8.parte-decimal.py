#Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.

numeroreal = float(input("Querido usuario ingrese un número real: "))

partedecimal = numeroreal % 1

print(f"La parte decimal de {numeroreal} es: {partedecimal}")