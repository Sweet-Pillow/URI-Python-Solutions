def main():
    N = int(input())
    for i in range(0, N):
        X, Y = input().split()
        X = int(X)
        Y = int(Y)
        impar = 0

        if X > Y:
            X, Y = Y, X

        for a in range(X+1, Y):
            if a % 2 != 0:
                impar += a

        print(impar)


if __name__ == '__main__':
    main()
