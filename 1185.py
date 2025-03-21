O = input()

M = []
aux = 11
soma = 0
quantidadeElementos = 0
linha = coluna = 12

for i in range(linha):
    M.append([])
    for j in range(coluna):
        auxf = float(input())
        M[i].append(auxf)

for i in range(0, linha - 1):
    for j in range(0, aux):
        soma = soma + M[i][j]
        quantidadeElementos = quantidadeElementos + 1
    aux = aux - 1 

if(O == "S"):
    print(soma)

else:
    print(round(soma/quantidadeElementos, 1))