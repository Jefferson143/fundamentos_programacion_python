'''
Clase:        Clase 11
Tema:         Matriz
Ejercicio:    10.2.1. Diagonal principal y secundaria
Descripción: Dada una matriz cuadrada ingresada por el
usuario, crea dos listas, una con los
elementos de la diagonal principal y la otra
con los elementos de la diagonal
secundaria.

Autor:        Jefferson Omar Escobar Estupinian
Fecha:        2025-06-14
Estado:       [ Terminado ]
'''
n = int(input("Tamaño de la matriz: "))

matriz = []
for i in range(n):
    fila = list(map(int, input(f"Fila {i+1} asegurate de separar con comas cada número4: ").split(',')))
    matriz.append(fila)


diagonal_principal = []
diagonal_secundaria = []

for i in range(n):
    diagonal_principal.append(matriz[i][i])
    diagonal_secundaria.append(matriz[i][n - 1 - i])

print("Diagonal principal:", diagonal_principal)
print("Diagonal secundaria:", diagonal_secundaria)