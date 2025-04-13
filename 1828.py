T = int(input())
valoresInput = []

def regras_pedra(escolha_adversario):
    match escolha_adversario:
        case 'pedra':
            return empate()
        
        case 'papel':
            return derrota()
        
        case 'tesoura':
            return vitoria()
        
        case 'lagarto':
            return vitoria()
        
        case 'Spock':
            return derrota()

def regras_papel(escolha_adversario):
    match escolha_adversario:
        case 'pedra':
            return vitoria()
        
        case 'papel':
            return empate()
        
        case 'tesoura':
            return derrota()
        
        case 'lagarto':
            return derrota()
        
        case 'Spock':
            return vitoria()

def regras_tesoura(escolha_adversario):
    match escolha_adversario:
        case 'pedra':
            return derrota()
        
        case 'papel':
            return vitoria()
        
        case 'tesoura':
            return empate()
        
        case 'lagarto':
            return vitoria()
        
        case 'Spock':
            return derrota()
        
def regras_lagarto(escolha_adversario):
    match escolha_adversario:
        case 'pedra':
            return derrota()
        
        case 'papel':
            return vitoria()
        
        case 'tesoura':
            return derrota()
        
        case 'lagarto':
            return empate()
        
        case 'Spock':
            return vitoria()

def regras_spock(escolha_adversario):
    match escolha_adversario:
        case 'pedra':
            return vitoria()
        
        case 'papel':
            return derrota()
        
        case 'tesoura':
            return vitoria()
        
        case 'lagarto':
            return derrota()
        
        case 'Spock':
            return empate()

def vitoria():
    return print('Bazinga!')

def derrota():
    return print('Raj trapaceou!')

def empate():
    return print('De novo!')

for _ in range(T):
    # valoresInput.append(list(map(str, input().split())))
    valoresInput.append(input())

for i, val in enumerate(valoresInput):
    print(f'Caso #{i+1}:', end=' ')

    sheldon, raj = val.split()

    match sheldon:
        case 'pedra':
            regras_pedra(raj)
        case 'papel':
            regras_papel(raj)
        case 'tesoura':
            regras_tesoura(raj)
        case 'lagarto':
            regras_lagarto(raj)
        case 'Spock':
            regras_spock(raj)
