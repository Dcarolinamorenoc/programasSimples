#Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:

cadena = input("Escribe un número entero de tres dígitos: ")
invertir = ""

for i in range(len(cadena)):
    invertir += cadena[-(i + 1)]
    
print("Número invertido:", invertir)