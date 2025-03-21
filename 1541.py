import math

test = True
aux = 0
valores = []

while test:
    entradas = input()
    valores.append(list(map(int, entradas.split())))

    if (len(list(map(int, entradas.split()))) == 1):
        test = False

for i in range(0, len(valores) - 1):
    print(int(math.sqrt(valores[i][0] * valores[i][1] * 100 / valores[i][2])))