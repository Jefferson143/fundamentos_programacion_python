'''
Clase:        Clase 11
Tema:         Matriz
Ejercicio:    10.3.2. Juego del entorno
Descripción: Dada una matriz binaria ingresada por el
usuario, verifica para cada celda de una
matriz binaria cuántos elementos con valor
de 1 hay en las celdas vecinas (arriba, abajo,
izquierda, derecha, diagonales).

Autor:        Jefferson Omar Escobar Estupinian
Fecha:        2025-06-14
Estado:      [Terminado]
'''
n = int(input("Número de filas: "))
m = int(input("Número de columnas: "))

matriz = []
for i in range(n):
    fila = list(map(int, input(f"Fila {i+1} acuerdate de separar con comas: ").split(',')))
    matriz.append(fila)

direcciones = [(-1, -1), (-1, 0), (-1, 1),
               (0, -1),          (0, 1),
               (1, -1), (1, 0),  (1, 1)]

resultado = []

for i in range(n):
    fila_resultado = []
    for j in range(m):
        suma_vecinos = 0
        for dx, dy in direcciones:
            ni, nj = i + dx, j + dy

            if 0 <= ni < n and 0 <= nj < m:
                if matriz[ni][nj] == 1:
                    suma_vecinos += 1
        fila_resultado.append(suma_vecinos)
    resultado.append(fila_resultado)

for fila in resultado:
    print(fila)