def main():
    V = int(input())
    N = [V]

    for i in range(1, 10):
        N.append(N[i-1] * 2)

    for j in range(0, 10):
        print(f'N[{j}] = {N[j]}')


if __name__ == '__main__':
    main()
