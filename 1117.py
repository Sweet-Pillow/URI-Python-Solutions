def main():

    while True:
        nota1 = float(input())

        if nota1 < 0 or nota1 > 10:
            print('nota invalida')

        else:
            break

    while True:
        nota2 = float(input())

        if nota2 < 0 or nota2 > 10:
            print('nota invalida')

        else:
            break

    print(f'media = {(nota1+nota2)/2:.2f}')


if __name__ == '__main__':
    main()
