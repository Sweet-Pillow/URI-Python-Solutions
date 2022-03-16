def main():
    a, b = input().split()
    a = int(a)
    b = int(b)

    print(f'O JOGO DUROU {(24-a+b) if a >= b else (b-a)} HORA(S)')


if __name__ == '__main__':
    main()
