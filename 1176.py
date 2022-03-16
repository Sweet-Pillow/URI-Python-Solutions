def main():
    T = int(input())

    for i in range(0, T):
        N = int(input())
        a = 0
        b = 1

        if N == 0:
            print('Fib(0) = 0')
            continue

        for j in range(0, N-1):
            a, b = b, a+b
            print(f'{a=} {b=}')

        print(f'Fib({N}) = {b}')


if __name__ == '__main__':
    main()
