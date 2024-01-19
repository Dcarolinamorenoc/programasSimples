#Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo. El promedio del ramo se calcula con la siguiente formula. NC=(C1+C2+C3)/3 ....NF=NC⋅0.7+NL⋅0.3 ...Donde NC es el promedio de certámenes, NL el promedio de laboratorio y NF la nota final.
#Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio, y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.

certamen1 = float(input("Ingrese la nota del primer certamen: "))
certamen2 = float(input("Ingrese la nota del segundo certamen: "))
laboratorio = float(input("Ingrese la nota de laboratorio: "))

certamenes = (certamen1 + certamen2) / 2

certamen3 = (60 - (certamenes * 0.7 + laboratorio * 0.3)) / 0.7

print(f"Para aprobar el ramo con nota final 60, necesitas obtener {certamen3:.2f} en el tercer certamen. Buena Suerte :) ")