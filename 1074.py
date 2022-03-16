def main():
    N = int(input())
    X = list([int(input()) for i in range(0, N)])

    for i in X:
        if i == 0:
            print('NULL')

        elif i % 2 == 0:
            if i > 0:
                print('EVEN POSITIVE')
            else:
                print('EVEN NEGATIVE')

        elif i > 0:
            print('ODD POSITIVE')
        else:
            print('ODD NEGATIVE')


if __name__ == '__main__':
    main()
