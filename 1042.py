def main():
    a, b, c = input().split()
    l = [int(a), int(b), int(c)]
    la = l.copy()
    la.sort()

    for i in la: print(i)

    print('')

    for i in l: print(i)


if __name__ == '__main__':
    main()
