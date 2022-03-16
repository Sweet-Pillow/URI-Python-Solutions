def main():
    num = list([int(input()) for i in range(0, 5)])
    print(f'{len(list(filter(lambda x: x % 2 == 0, num)))} valor(es) par(es)')
    print(f'{len(list(filter(lambda x: x % 2 != 0, num)))} valor(es) impar(es)')
    print(f'{len(list(filter(lambda x: x > 0, num)))} valor(es) positivo(s)')
    print(f'{len(list(filter(lambda x: x < 0, num)))} valor(es) negativo(s)')


if __name__ == '__main__':
    main()
