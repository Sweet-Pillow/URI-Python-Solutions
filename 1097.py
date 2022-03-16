def main():
    i = 1
    j = 7

    while i <= 9:
        for a in range(0, 3):
            print(f'I={i} J={j-a}')

        i += 2
        j += 2


if __name__ == '__main__':
    main()
