def main():
    X = int(input())
    Y = int(input())

    if X > Y:
        X, Y = Y, X

    for i in range(X+1, Y):
        if i % 5 in (2, 3):
            print(i)


if __name__ == '__main__':
    main()
