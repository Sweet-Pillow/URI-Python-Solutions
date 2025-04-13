def stringParaBin(str):
    valor = 0
    for index, value in enumerate(str):
        valor += int(value) * (2**(len(str)-index-1))
    
    return valor

valores_input = []
contagem_caw = 0

while contagem_caw < 3:
    entrada = input()
    valores_input.append(entrada)
    if (entrada == "caw caw"):
        contagem_caw += 1
    
for i in range(3):
    index = valores_input.index("caw caw")
    valor_total = 0

    for i in valores_input[:index]:
        aux = i.replace("-", "0").replace("*", "1")
        valor_total += stringParaBin(aux)
    
    print(valor_total)
    del valores_input[:index+1]