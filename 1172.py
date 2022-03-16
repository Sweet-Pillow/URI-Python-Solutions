def main():
    X = list()

    for i in range(0, 10):
        A = int(input())

        if A <= 0:
            A = 1

        X.append(A)

    for j in range(0, 10):
        print(f'X[{j}] = {X[j]}')


if __name__ == '__main__':
    main()
