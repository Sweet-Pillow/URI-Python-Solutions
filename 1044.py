def main():
    A, B = input().split()
    A = int(A)
    B = int(B)

    if A % B == 0 or B % A == 0:
        print('Sao Multiplos')

    else:
        print('Nao sao Multiplos')


if __name__ == '__main__':
    main()