'''
Clase:        Clase 11
Tema:         Matriz
Ejercicio:    10.3.1. Matriz simétrica
Descripción: Dada una matriz cuadrada ingresada por el
usuario, comprueba si la matriz cuadrada es
simétrica respecto a su diagonal principal.

Autor:        Jefferson Omar Escobar Estupinian
Fecha:        2025-06-14
Estado:      [Terminado]
'''
n = int(input("Tamaño de la matriz: "))

matriz = []
for i in range(n):
    fila = list(map(int, input(f"Fila {i+1} recuerda separar con comas: ").split(',')))
    matriz.append(fila)

es_simetrica = True

for i in range(n):
    for j in range(n):
        if matriz[i][j] != matriz[j][i]:
            es_simetrica = False
            break

if es_simetrica:
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")