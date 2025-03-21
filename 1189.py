O = input()

M = []
aux = 0
soma = 0
quantidadeElementos = 0
linha = coluna = 12

inicioLin = 1
fimLin = 10

for i in range(linha):
    M.append([])
    for j in range(coluna):
        auxf = float(input())
        M[i].append(auxf)

while aux <= 4:
    for i in range(inicioLin, fimLin + 1):
        soma = soma + M[i][aux]
        quantidadeElementos = quantidadeElementos + 1

    inicioLin = inicioLin + 1
    fimLin = fimLin - 1
    aux = aux + 1

if(O == "S"):
    print(soma)

else:
    print(round(soma/quantidadeElementos, 1))