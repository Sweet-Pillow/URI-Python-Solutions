def main():
    O = input()
    T = 12
    M = []
    L = [''] * T
    soma = 0

    for i in range(0, T):
        for j in range(0, T):
            L[j] = float(input())

        M.append(L)

    cont = 1
    for i in range(1, T):
        for j in range(0, cont):
            print(M[i][j])
            soma += M[i][j]

        cont += 1

    if O == 'S':
        print(f'{soma:.1f}')

    elif O == 'M':
        print(f'{soma/66:.1f}')
        #66
    print(M)


if __name__ == '__main__':
    main()
