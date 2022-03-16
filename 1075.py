def main():
    N = int(input())
    cont = 0

    for i in range(1, 10000):
        if i % N == 2:
            print(i)


if __name__ == '__main__':
    main()
