O = input()

M = []
aux = 11
soma = 0
quantidadeElementos = 0
linha = coluna = 12

inicioCol = 1
fimCol = 10

for i in range(linha):
    M.append([])
    for j in range(coluna):
        auxf = float(input())
        M[i].append(auxf)

while aux >= 7:
    for j in range(inicioCol, fimCol + 1):
        soma = soma + M[aux][j]
        quantidadeElementos = quantidadeElementos + 1

    inicioCol = inicioCol + 1
    fimCol = fimCol - 1
    aux = aux - 1

if(O == "S"):
    print(soma)

else:
    print(round(soma/quantidadeElementos, 1))