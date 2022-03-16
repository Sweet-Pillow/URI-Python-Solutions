def main():
    n, x = list(map(int, input().split()))
    tamanho = input()
    p, m, g = list(map(int, input().split()))
    posi_p = 0
    posi_m = 0
    posi_g = 0
    muralhas = [x]
    conta = 1

    for i in tamanho:
        if i == 'P':
            while True:
                if muralhas[posi_p] >= p:
                    muralhas[posi_p] -= p
                    break

                else:
                    if len(muralhas) == posi_p+1:
                        muralhas.append(x-p)
                        conta +=1
                        break

                    else:
                        posi_p += 1


        if i == 'M':
            while True:
                if muralhas[posi_m] >= m:
                    muralhas[posi_m] -= m
                    break

                else:
                    if len(muralhas) == posi_m+1:
                        muralhas.append(x - m)
                        conta += 1
                        break

                    else:
                        posi_m += 1

        if i == 'G':
            while True:
                if muralhas[posi_g] >= g:
                    muralhas[posi_g] -= g
                    break

                else:
                    if len(muralhas) == posi_g+1:
                        muralhas.append(x - g)
                        conta += 1
                        break

                    else:
                        posi_g += 1
                        
    print(conta)


if __name__ == '__main__':
    main()
