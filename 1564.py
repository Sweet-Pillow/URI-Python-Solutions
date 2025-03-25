valoresInput = []

while True:
    try:
        N = int(input())
        valoresInput.append(N)
        
    except EOFError:
        break

    except ValueError:
        break

for elem in valoresInput:
    if elem != 0:
        print("vai ter duas!")

    else:
        print("vai ter copa!")