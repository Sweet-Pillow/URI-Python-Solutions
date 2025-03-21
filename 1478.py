N = int(input())
valoresInput = []

while N != 0:
    valoresInput.append(N)
    N = int(input())
    
def matriz_ass(num):
    inicioCol = 0

    M = [[0 for _ in range(num)] for _ in range(num)]

    for i in range(0, num):
        aux = 1
        for j in range(inicioCol, num):
            M[i][j] = aux
            M[j][i] = aux
            aux+= 1       
        inicioCol+= 1

    for i in range(0, num):
        for j in range(0, num):
            if j == 0:
                print(f'{M[i][j]:>3}', end='')
            else:
                print(f'{M[i][j]:>4}', end='')
        print("")

    print("")


for n in valoresInput:
    matriz_ass(n)
