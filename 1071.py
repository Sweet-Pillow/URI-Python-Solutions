def main():
    X = int(input())
    Y = int(input())
    cont = 0

    if X > Y: X, Y = Y, X

    for i in range(X + 1, Y):
        if i % 2 != 0:
            cont += i

    print(cont)

if __name__ == '__main__':
    main()
