#Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c del triangulo, dado por el teorema de Pitágoras: c2=a2+b2

import math

catetoa = float(input("Escriba el valor del cateto A: "))
catetob = float(input("Escriba el valor del cateto B: "))

hipotenusa = math.sqrt(catetoa**2 + catetob**2)

print("El valor de la hipotenusa de este triángulo es de:", hipotenusa)