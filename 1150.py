def main():
    X = int(input())
    cont = 1
    i = X + 1
    while True:
        Z = int(input())

        if Z > X:
            while X < Z:
                X += i
                i += 1
                cont += 1

            break

    print(cont)


if __name__ == '__main__':
    main()
