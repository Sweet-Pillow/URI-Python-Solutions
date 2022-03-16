def main():

    S = 0

    for i in range(1, 101):
        S += 1/i

    print(f'{S:.2f}')


if __name__ == '__main__':
    main()
