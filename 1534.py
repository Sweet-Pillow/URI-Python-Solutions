valoresInput = []

while True:
    try:
        N = int(input())
        valoresInput.append(N)
        
    except EOFError:
        break

    except ValueError:
        break


def matriz(num):
    M = [[3 for _ in range(num)] for _ in range(num)]

    for prin in range(0, num):
        M[prin][prin] = 1
    
    for index, sec in enumerate(range(num, 0, -1)):
        M[index][sec - 1] = 2

    for linha in M:
        for coluna in linha:
            print(coluna, end='')
        
        print()


for elem in valoresInput:
    matriz(elem)