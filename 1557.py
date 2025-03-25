N = int(input())
valoresInput = []

while N != 0:
    valoresInput.append(N)
    N = int(input())


def matriz_quadrada(num):

    espacos = len(str(2**((num - 1)*2)))
    for i in range(0, num):
        for j in range(0, num):
            if j == 0:
                print(f'{2**(j + i):>{espacos}}', end='')
            else:
                print(f'{2**(j + i):>{espacos + 1}}', end='')
        print("")

    print("")


for elem in valoresInput:
    matriz_quadrada(elem)