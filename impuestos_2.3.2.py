unidades = int(input("Ingrese las unidades consumidas: "))

impuesto = 0

if unidades <= 100:
    impuesto = 0
elif unidades <= 200:
    unidades_con_impuesto = unidades - 100
    impuesto = unidades_con_impuesto * 0.5
else:
    impuesto = (100 * 0.5) + ((unidades - 200) * 0.7)

print("Impuesto aplicado: $", impuesto)