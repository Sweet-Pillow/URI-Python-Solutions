
def matriz_quadrada(num):
    M = [[0 for _ in range(num)] for _ in range(num)]

    camada = 0

    while camada <= -(-num // 2) - 1:
        for c in range(camada, num - camada):
            M[camada][c] = camada + 1
            M[c][camada] = camada + 1

        for l in range(camada + 1, num - camada):
            M[l][num - camada - 1] = camada + 1
            M[num - camada - 1][l] = camada + 1

        camada+=1

    for i in range(0, num):
        for j in range(0, num):
            if j == 0:
                print(f'{M[i][j]:>3}', end='')
            else:
                print(f'{M[i][j]:>4}', end='')
        print("")

    print("")

N = int(input())
valoresInput = []

while N != 0:
    valoresInput.append(N)
    N = int(input())

for v in valoresInput:
    matriz_quadrada(v)