def main():
    N = int(input())

    for i in range(0, N):
        X = int(input())
        cont = 0

        for j in range(1, X):
            if X % j == 0:
                cont += 1

        if cont == 1:
            print(f'{X} eh primo')

        else:
            print(f'{X} nao eh primo')


if __name__ == '__main__':
    main()
