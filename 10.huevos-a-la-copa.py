#Cuando un huevo es hervido en agua, las proteínas comienzan a coagularse cuando la temperatura sobrepasa un punto crítico. A medida que la temperatura aumenta, las reacciones se aceleran. En la clara, las proteínas comienzan a coagularse para temperaturas sobre 63°C, mientras que en la yema lo hacen para temperaturas sobre 70°C. Para hacer un huevo a la copa, la clara debe haber sido calentada lo suficiente para coagularse a más de 63°C, pero la yema no debe sobrepasar los 70°C para evitar obtener un huevo duro.
#Escriba un programa que reciba como entrada la temperatura original del huevo y muestre como salida el tiempo en segundos que le toma alcanzar la temperatura máxima para prepararlo a la copa.

import math

TH = float(input("Temperatura original del huevo\n"))

TE=100

M=47

P=1.638

C=3.7

K=0.0054

dividendo = math.pow(M, (2/3)) * (C * (math.pow(P, (1/3))))

divisor = (K * math.pow(math.pi, 2)) * math.pow((4*math.pi) / 3, (2/3))

resultado = dividendo / divisor

resultado2 = math.log(0.76 * ((TH - TE) / (70 - TE)))

segundos = resultado * resultado2

minutos = round(segundos/60)

print(f"El tiempo máximo para prepararlo a la copa son {round (segundos)} segundos") 

print(f"El tiempo máximo para prepararlo a la copa son {minutos} minutos")