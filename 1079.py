def main():
    N = int(input())

    for i in range(0, N):
        num = list(input().split())
        num = list(map(float, num))
        print(f'{(num[0]*2 + num[1]*3 + num[2]*5) / 10:.1f}')


if __name__ == '__main__':
    main()
