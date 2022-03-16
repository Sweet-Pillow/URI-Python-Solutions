def main():
    N = int(input())
    X = list([int(input()) for i in range(0, N)])
    entrada = 0
    saida = 0

    for i in X:
        if i >= 10 and i <= 20:
            entrada += 1

        else:
            saida += 1

    print(f'{entrada} in')
    print(f'{saida} out')


if __name__ == '__main__':
    main()
