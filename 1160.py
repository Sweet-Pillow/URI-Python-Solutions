def main():
    T = int(input())

    for i in range(0, T):
        PA, PB, G1, G2 = input().split()
        PA = int(PA)
        PB = int(PB)
        G1 = float(G1)
        G2 = float(G2)
        count = 0

        while PA <= PB and count < 101:
            PA += (PA * G1)//100
            PB += (PB * G2)//100
            print(count)
            count += 1

        if count > 100:
            print('Mais de 1 seculo.')

        else:
            print(f'{count} anos.')


if __name__ == '__main__':
    main()
