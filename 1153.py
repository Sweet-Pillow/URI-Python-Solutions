def main():
    N = int(input())
    A = 1

    for i in range(1, N + 1):
        A = i * A

    print(A)


if __name__ == '__main__':
    main()
