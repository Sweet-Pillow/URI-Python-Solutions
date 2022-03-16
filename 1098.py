def main():
    i = 0
    j = 1

    while i <= 2:
        for a in range(0, 3):
            print(f'I={int(i) if int(i) == i else i} ', end='')
            print(f'J={int(j+a) if int(j+a) == j+a else j+a}')

        i += 0.2
        j += 0.2
        i = round(i, 1)
        j = round(j, 1)


if __name__ == '__main__':
    main()
