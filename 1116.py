def main():
    N = int(input())

    for i in range(0, N):
        X, Y = input().split()
        X = int(X)
        Y = int(Y)

        if Y == 0:
            print('divisao impossivel')

        else:
            print(f'{X/Y:.1f}')

if __name__ == '__main__':
    main()
