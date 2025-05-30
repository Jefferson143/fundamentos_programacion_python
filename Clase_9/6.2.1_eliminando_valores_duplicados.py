'''
Clase:        Clase 9
Tema:         Listas
Ejercicio:    6.2.1 eliminando valores duplicados
Descripción:  Dada una lista ingresada por el usuario, elimina los elementos duplicados
manteniendo la primera aparición de cada número.

Autor:        Jefferson Omar Escobar Estupinian
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''
lista = list(map(int, input("Dame la lista de tus numeros para eliminar los duplicados ").split()))
duplicados = [ ]
for numero in lista:
    if numero not in duplicados:
        duplicados.append(numero)
print(duplicados)
    