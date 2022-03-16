def main():
    N = int(input())
    X = list(map(int, input().split()))

    print(f'Menor valor: {min(X)}\n'
          f'Posicao: {X.index(min(X))}')


if __name__ == '__main__':
    main()
