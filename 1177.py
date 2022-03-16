def main():
    T = int(input())
    N = list()

    for i in range(0, 1000):
        for j in range(0, T):
            N.append(j)

    for x in range(0, 1000):
        print(f'N[{x}] = {N[x]}')


if __name__ == '__main__':
    main()
