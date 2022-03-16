def main():
    N = int(input())
    a = 0
    b = 1

    print(f'{a} ', end='')
    for i in range(0, N - 2):

        print(f'{b} ', end='')
        a, b = b, (a + b)

    print(f'{b}')


if __name__ == '__main__':
    main()
