from math import fabs

def main():
    A, B, C = input().split()
    A = float(A)
    B = float(B)
    C = float(C)

    if fabs(B-C)<A<B+C and fabs(A-C)<B<A+C and fabs(A-B)<C<A+B:
        print(f'Perimetro = {A + B + C}')

    else:
        print(f'Area = {((A + B) * C) / 2}')


if __name__ == '__main__':
    main()
