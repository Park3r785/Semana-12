
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


def labcam(f, c):

    # Verificar si salimos de la matriz
    if f >= N or c >= N:
        return 0

    # Verificar si encontramos un obstaculo
    if matriz[f][c] == 1:
        return 0

    # CASO BASE: Llegamos al destino
    if f == N - 1 and c == N - 1:
        return 1

    # CASOS RECURSIVOS

    # Si estamos en la ultima fila, solo podemos avanzar a la derecha
    if f == N - 1:
        return labcam(f, c + 1) + 0

    # Si estamos en la ultima columna, solo podemos avanzar hacia abajo
    elif c == N - 1:
        return 0 + labcam(f + 1, c)

    # Podemos avanzar a la derecha o hacia abajo
    else:
        return labcam(f, c + 1) + labcam(f + 1, c)


# Mostrar la matriz
print("LABERINTO:")
for fila in matriz:
    print(fila)

# Iniciar desde la posicion (0, 0)
resultado = labcam(0, 0)

print("\nCantidad de caminos posibles:", resultado)

