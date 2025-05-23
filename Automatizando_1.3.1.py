cuenta= float(input("Total fr la cuenta: "))
porcentaje= float(input("Porcentaje de la propina"))

propina= cuenta * (porcentaje / 100)
total= cuenta + propina

print("Propina:",propina)
print("Total de la cuenta con propina:",total)
