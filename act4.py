#Convertidor de cm a shakus y kens
#1 ken son 6 shakus
#1 shaku son 30.3 cm

# -*- coding: utf-8 -*-

cm = float(input("Introduce centímetros: "))
shaku = cm / 30.3
ken = shaku / 6

print(f"{cm} centímetros equivalen a {round(shaku,2)} shakus y {round(ken,2)} kens")

