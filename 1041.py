def main():
    x, y = input().split()
    x = round(float(x), 1)
    y = round(float(y), 1)

    if x > 0 and y > 0:
        print('Q1')

    elif x > 0 and y < 0:
        print('Q4')

    elif x < 0 and y > 0:
        print('Q2')

    elif x < 0 and y < 0:
        print('Q3')

    elif x == 0 and y != 0:
        print('Eixo Y')

    elif x != 0 and y == 0:
        print('Eixo X')

    else:
        print('Origem')


if __name__ == '__main__':
    main()
