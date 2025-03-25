valoresInput = []

while True:
    try:
        L = int(input())

        valoresInput.append(list(map(int, input().split(' '))))

    except EOFError:
        break

    except ValueError:
        break

for lesma in valoresInput:
    rapida = max(lesma)

    if(rapida < 10):
        print('1')
    elif rapida >= 10 and rapida < 20:
        print('2')
    else:
        print('3')