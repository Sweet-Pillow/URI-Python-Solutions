def feliz():
    return print(':)')

def triste():
    return print(':(')

def casos(a, b, c):
    # Caso 1
    if ((a > b) and (c >= b)):
        return feliz()

    # Caso 2
    if ((a < b) and (c <= b)):
        return triste()

    if (a < b < c):
        # Caso 3
        if((a - b) < (b - c)):
            return triste()
        
        else:
            # Caso 4
            return feliz()
    
    if (a > b > c):
        # Caso 5
        if((a - b) > (b - c)):
            return feliz()
        
        else:
            # Caso 6
            return triste()
    
    # Caso 7
    if ((a == b) and (b < c)):
        return feliz()
    
    # Caso 8
    if ((a == b) and (b >= c)):
        return triste()
    


A, B, C = list(map(int, input().split()))

casos(A, B, C)