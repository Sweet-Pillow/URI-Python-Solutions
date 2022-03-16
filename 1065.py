def main():
    par = 0
    for i in range(0, 5):
        if int(input()) % 2 == 0:
            par += 1

    print(f'{par} valores pares')


if __name__ == '__main__':
    main()
