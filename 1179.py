def verificar(tipo, vetor):
    for j in range(0, len(vetor)):
        print(f'{tipo}[{j}] = {vetor[j]}')
    vetor.clear()


def main():
    par = list()
    impar = list()
    t = 0

    while t < 2:
        x = int(input())

        if x % 2 == 0:
            par.append(x)

        else:
            impar.append(x)

        if len(par) == 5:
            verificar('par', par)
            t += 1

        if len(impar) == 5:
            verificar('impar', impar)
            t += 1

    for i in range(0, 5-len(impar)-len(par)):
        x = int(input())

        if x % 2 == 0:
            par.append(x)

        else:
            impar.append(x)

    verificar('impar', impar)
    verificar('par', par)


if __name__ == '__main__':
    main()
