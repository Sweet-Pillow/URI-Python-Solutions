valoresInput = []

while True:
    try:
        N = int(input())

        valoresInput.append(N)

    except EOFError:
        break

    except ValueError:
        break

def matriz_quadrada(num):
    inicioUns = num//3
    centro = -(-num//2) - 1
    M = [[0 for _ in range(num)] for _ in range(num)]
    
    for i in range(num):
        M[i][i] = 2
        M[i][num - i - 1] = 3

    for i in range(inicioUns, num - inicioUns):
        for j in range(inicioUns, num - inicioUns):
            M[i][j] = 1
    
    M[centro][centro] = 4

    for lin in M:
        for col in lin:
            print(col, end='')
        print()
    print()

for elem in valoresInput:
    matriz_quadrada(elem)