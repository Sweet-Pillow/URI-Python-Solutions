def main():
    while True:
        alcool = 0
        gasolina = 0
        diesel = 0

        while True:
            x = int(input())

            if x == 1:
                alcool += 1

            elif x == 2:
                gasolina += 1

            elif x == 3:
                diesel += 1

            elif x == 4:
                break

        print('MUITO OBRIGADO\n'
              f'Alcool: {alcool}\n'
              f'Gasolina: {gasolina}\n'
              f'Diesel: {diesel}')

        break


if __name__ == '__main__':
    main()
