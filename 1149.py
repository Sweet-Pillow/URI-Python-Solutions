def main():
    X = list(map(int, input().split()))

    for i in range(1, len(X)):
        if X[i] > 0:
            print(f'{sum(range(X[0], X[0] + X[i]))}')
            break



if __name__ == '__main__':
    main()
