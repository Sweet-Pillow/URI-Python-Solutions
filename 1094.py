def main():
    N = int(input())
    cobaias = list([input() for i in range(0, N)])
    r, s, c = 0, 0, 0

    for i in cobaias:
        if 'R' in i:
            r += int(i.split()[0])

        elif 'S' in i:
            s += int(i.split()[0])

        else:
            c += int(i.split()[0])

    print(f'Total: {r+s+c} cobaias')
    print(f'Total de coelhos: {c}')
    print(f'Total de ratos: {r}')
    print(f'Total de sapos: {s}')
    print(f'Percentual de coelhos: {(c*100) / (r+s+c):.2f} %')
    print(f'Percentual de ratos: {(r*100) / (r+s+c):.2f} %')
    print(f'Percentual de sapos: {(s*100) / (r+s+c):.2f} %')


if __name__ == '__main__':
    main()
