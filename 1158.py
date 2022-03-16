def main():
    N = int(input())

    for i in range(0, N):
        X, Y = input().split()
        X = int(X)
        Y = int(Y)

        if X % 2 == 0:
            X += 1

        print(sum(range(X, X + (2*Y), 2)))


if __name__ == '__main__':
    main()
