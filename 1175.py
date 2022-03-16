def main():
    N = list()
    aux = 19

    for i in range(0, 20):
        N.append(int(input()))

    for j in range(0, 10):
        N[j], N[aux] = N[aux], N[j]
        aux -= 1

    for x in range(0, 20):
        print(f'N[{x}] = {N[x]}')


if __name__ == '__main__':
    main()
