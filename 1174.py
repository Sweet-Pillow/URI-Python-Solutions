def main():
    A = list()

    for i in range(0, 100):
        A.append(float(input()))

    for j in range(0, 100):
        if A[j] <= 10:
            print(f'A[{j}] = {A[j]:.1f}')


if __name__ == '__main__':
    main()
