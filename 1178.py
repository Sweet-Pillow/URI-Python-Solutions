def main():
    X = float(input())
    N = [X]

    for i in range(0, 99):
        N.append(N[i]/2)

    for j in range(0, 100):
        print(f'N[{j}] = {N[j]:.4f}')


if __name__ == '__main__':
    main()
