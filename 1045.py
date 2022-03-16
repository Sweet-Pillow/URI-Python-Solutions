def main():
    A, B, C = input().split()
    l = [float(A), float(B), float(C)]
    l.sort(reverse=True)
    A = l[0]
    B = l[1]
    C = l[2]

    if A >= B + C:
        print('NAO FORMA TRIANGULO')

    else:

        if A*A == B*B + C*C:
            print('TRIANGULO RETANGULO')

        elif A*A > B*B + C*C:
            print('TRIANGULO OBTUSANGULO')
            trian(A, B, C)

        elif A*A < B*B + C*C:
            print('TRIANGULO ACUTANGULO')
            trian(A, B, C)


def trian(A, B, C):
    if A == B == C:
        print('TRIANGULO EQUILATERO')

    elif A == B or A == C or B == C:
        print('TRIANGULO ISOSCELES')


if __name__ == '__main__':
    main()
