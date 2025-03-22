O = input()

M = []
soma = 0
quantidadeElementos = 0
linha = coluna = aux = 12

for i in range(linha):
    M.append([])
    for j in range(coluna):
        auxf = float(input())
        M[i].append(auxf)

for i in range(1, linha):
    for j in range(aux-1, coluna):
        soma = soma + M[i][j]
        quantidadeElementos = quantidadeElementos + 1
    aux = aux - 1 

if(O == "S"):
    print(soma)

else:
    print(round(soma/quantidadeElementos, 1))