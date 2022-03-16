def main():
    animal = list()
    for i in range(0, 3):
        animal.append(input())

    if animal[0] == 'vertebrado':
        if animal[1] == 'ave':
            if animal[2] == 'carnivoro':
                print('aguia')
            elif animal[2] == 'onivoro':
                print('pomba')

        elif animal[1] == 'mamifero':
            if animal[2] == 'onivoro':
                print('homem')
            elif animal[2] == 'herbivoro':
                print('vaca')

    elif animal[0] == 'invertebrado':
        if animal[1] == 'inseto':
            if animal[2] == 'hematofago':
                print('pulga')
            elif animal[2] == 'herbivoro':
                print('lagarta')

        elif animal[1] == 'anelideo':
            if animal[2] == 'hematofago':
                print('sanguessuga')
            elif animal[2] == 'onivoro':
                print('minhoca')


if __name__ == '__main__':
    main()
