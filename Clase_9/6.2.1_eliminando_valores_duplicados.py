lista = list(map(int, input("Dame la lista de tus numeros para eliminar los duplicados ").split()))
duplicados = [ ]
for numero in lista:
    if numero not in duplicados:
        duplicados.append(numero)
print(duplicados)
    