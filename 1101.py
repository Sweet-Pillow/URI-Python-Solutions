def main():

    while True:
        M, N = list(map(int, input().split()))

        if M > 0 and N > 0:
            if M < N:
                M, N = N, M

            for i in range(N, M+1):
                print(f'{i} ', end='')
            print(f'Sum={sum(range(N, M+1))}')

        else:
            break


if __name__ == '__main__':
    main()
