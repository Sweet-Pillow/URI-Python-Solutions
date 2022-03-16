def main():

    n1, n2, n3, n4 = input().split()

    m = round((float(n1)*2 + float(n2)*3 + float(n3)*4 + float(n4)*1) / 10, 1)

    print(f'Media: {m}')

    if m >= 7.0:
        print('Aluno aprovado.')

    elif m < 5.0:
        print('Aluno reprovado.')

    else:
        print('Aluno em exame.')

        e = float(input())

        print(f'Nota do exame: {e}')

        me = round((m + e) / 2, 1)

        if me >= 5.0:
            print('Aluno aprovado.')

        else:
            print('Aluno Reprovado.')

        print(f'Media final: {me}')


if __name__ == '__main__':
    main()
