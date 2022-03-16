def main():
    while True:
        X, Y = input().split()
        X = int(X)
        Y = int(Y)

        if X == Y:
            break

        if X > Y:
            print('Decrescente')

        else:
            print('Crescente')


if __name__ == '__main__':
    main()
