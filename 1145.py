def main():
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
    A = 0

    for i in range(1, Y + 1):
        print(f'{i}', end='')
        A += 1
        if A < X:
            print(' ', end='')

        elif A == X:
            print()
            A = 0


if __name__ == '__main__':
    main()
