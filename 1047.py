def main():
    a, b, c, d = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)

    dhor = 0
    dmin = 0

    # Calculando as horas
    if a >= c:
        dhor = 24 - a + c

    else:
        dhor = c - a

    #Calculando os min
    if b > d:
        dmin = 60 - b + d
        dhor = dhor - 1
    else:
        dmin = d - b

    if dhor == 24 and dmin != 0:
        dhor = 0

    print(f'O JOGO DUROU {dhor} HORA(S) E {dmin} MINUTO(S)')


if __name__ == '__main__':
    main()
