def main():
    while True:
        X = int(input())

        if X == 0:
            break

        if X % 2 != 0:
            X += 1

        print(sum(range(X, X + 10, 2)))


if __name__ == '__main__':
    main()
