'''
Clase:        Clase 9
Tema:         Listas
Ejercicio:    6.3.1 numeros lideres
Descripción:  Un número en una lista es "líder" si es
estrictamente mayor que todos los
elementos a su derecha. Dada una lista de
números ingresada por el usuario, imprime
todos los números líderes.

Autor:        Jefferson Omar Escobar Estupinian
Fecha:        2025-06-02
Estado:       [ Terminado ]
'''
numeros = list(map(int, input("Escribe los números: ").split()))

lideres = []

mayor = -1

for numero in reversed(numeros):
    if numero > mayor:
        lideres.append(numero)  
        mayor = numero 

lideres.reverse()

print(" ".join(map(str, lideres)))
