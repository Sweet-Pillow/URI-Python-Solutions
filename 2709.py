def main():
    M = int(input())
    V = list([int(input()) for i in range(0, M)])
    N = int(input())
    soma = 0
    prim = 0

    for i in range(len(V) - 1, -1, -N):
        soma += V[i]

    if soma == 1:
        prim += 1

    else:
        for j in range(2, soma):
            if soma % j == 0:
                prim += 1

    if prim == 0:
        print('You’re a coastal aircraft, Robbie, a large silver aircraft.')

    else:
        print('Bad boy! I’ll hit you.')


if __name__ == '__main__':
    while True:
        try:
            main()

        except EOFError:
            break
