
matriz = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

N = len(matriz)

# Crear matriz auxiliar
dp = [[0] * N for _ in range(N)]

# Recorrer desde abajo hacia arriba
for f in range(N - 1, -1, -1):

    # Recorrer desde derecha hacia izquierda
    for c in range(N - 1, -1, -1):

        # Si encontramos un obstaculo
        if matriz[f][c] == 1:
            dp[f][c] = 0

        # Caso base: llegamos al destino
        elif f == N - 1 and c == N - 1:
            dp[f][c] = 1

        else:
            derecha = 0
            abajo = 0

            # Verificar si podemos avanzar a la derecha
            if c + 1 < N:
                derecha = dp[f][c + 1]

            # Verificar si podemos avanzar hacia abajo
            if f + 1 < N:
                abajo = dp[f + 1][c]

            # Sumar los caminos posibles
            dp[f][c] = derecha + abajo


# Mostrar matriz original
print("LABERINTO:")
for fila in matriz:
    print(fila)

# Mostrar matriz de programacion dinamica
print("\nMATRIZ DP:")
for fila in dp:
    print(fila)

# Resultado final
print("\nCantidad de caminos:", dp[0][0])
