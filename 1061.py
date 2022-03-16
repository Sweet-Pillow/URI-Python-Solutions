def main():
    diaent = list(map(int, filter(lambda x: x.isdigit(), input().split())))
    horent = list(map(int, filter(lambda x: x.isdigit(), input().split())))
    diasai = list(map(int, filter(lambda x: x.isdigit(), input().split())))
    horsai = list(map(int, filter(lambda x: x.isdigit(), input().split())))

    dia = 0
    hor = 0
    min = 0
    seg = 0

    #Verifica segundo
    if horent[2] <= horsai[2]:
        seg = horsai[2] - horent[2]

    else:
        seg = 60 + horsai[2] - horent[2]
        min = -1

    #Verifica minutos
    if horent[1] <= horsai[1] + min:
        min = horsai[1] - horent[1]

    else:
        min = 60 - horent[1] + horsai[1] + min
        hor = - 1

    #Verifica horas
    if horent[0] <= horsai[0] + hor:
        hor = horsai[0] - horent[0] + hor

    else:
        hor = 24 - horent[0] + horsai[0] + hor
        dia = dia - 1

    #Verifica dias
    dia = diasai[0] - diaent[0] + dia

    print(f'{dia} dia(s)')
    print(f'{hor} hora(s)')
    print(f'{min} minuto(s)')
    print(f'{seg} segundo(s)')

if __name__ == '__main__':
    main()
