def main():
    S = 0
    numerador = 1
    denominador = 1

    while True:
        S += numerador/denominador
        numerador += 2
        denominador *= 2

        if numerador == 39:
            break

    print(f'{S:.2f}')


if __name__ == '__main__':
    main()
