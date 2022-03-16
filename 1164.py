def main():
    N = int(input())

    for i in range(0, N):
        X = int(input())
        cont = 0

        for j in range(1, X):
            if X % j == 0:
                cont += j

        if cont == X:
            print(f'{X} eh perfeito')

        else:
            print(f'{X} nao eh perfeito')


if __name__ == '__main__':
    main()
