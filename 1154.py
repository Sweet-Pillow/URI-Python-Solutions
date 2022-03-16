def main():
    idade = list()

    while True:
        aux = int(input())
        if aux < 0:
            break

        idade.append(aux)

    print(f'{sum(idade)/len(idade):.2f}')


if __name__ == '__main__':
    main()
