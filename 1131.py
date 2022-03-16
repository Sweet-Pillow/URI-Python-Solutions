def main():
    inter = 0
    gremio = 0
    empate = 0

    while True:
        i, g = input().split()
        i = int(i)
        g = int(g)

        if i > g:
            inter += 1

        elif g > i:
            gremio += 1

        else:
            empate += 1

        print('Novo grenal (1-sim 2-nao)')
        check = int(input())

        if check != 1:
            print(f'{inter+gremio+empate} grenais\n'
                  f'Inter:{inter}\n'
                  f'Gremio:{gremio}\n'
                  f'Empates:{empate}')

            if inter > gremio:
                print('Inter venceu mais')

            elif gremio > inter:
                print('Gremio venceu mais')

            else:
                print('Nao houve vencedor')

            break


if __name__ == '__main__':
    main()
