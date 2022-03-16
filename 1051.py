def main():
    salario = round(float(input()), 2)
    aux = 0

    if salario <= 2000.00:
        print('Isento')

    else:
        if salario > 4500.00:
            aux = (salario - 4500) * (28/100) + aux
            salario = salario - (salario - 4500)

        if salario > 3000.00 and salario <= 4500.00:
            aux = (salario - 3000.00) * (18/100) + aux
            salario = salario - (salario - 3000.00)

        if salario > 2000.00 and salario <= 3000.00:
            aux = (salario - 2000.00) * (8/100) + aux
            salario = aux
            print(f'R$ {salario:.2f}')


if __name__ == '__main__':
    main()
