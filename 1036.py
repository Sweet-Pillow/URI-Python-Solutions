from math import sqrt

def main():
    A, B, C = input().split(' ')
    A = float(A)
    B = float(B)
    C = float(C)
    D = 4*A*C
    if A == 0 or B*B < D:
        print('Impossivel calcular')

    else:
        print(f'R1 = {(-B+sqrt(B*B-D)) / (2*A):.5f}')
        print(f'R2 = {(-B-sqrt(B*B-D)) / (2*A):.5f}')


if __name__ == '__main__':
    main()
