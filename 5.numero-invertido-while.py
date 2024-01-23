#Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:

cadena = input("Escribe un número entero de tres dígitos: ")
invertir = ""

i = 0
while i < len(cadena):
    invertir += cadena[-(i + 1)]
    i += 1

print("Número invertido:", invertir)