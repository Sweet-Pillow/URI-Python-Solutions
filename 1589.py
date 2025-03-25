casos = int(input())

valoresInput = []

for i in range(casos):
    valoresInput.append(list(map(int, input().split())))

for raio in valoresInput:
    print(raio[0] + raio[1])
    