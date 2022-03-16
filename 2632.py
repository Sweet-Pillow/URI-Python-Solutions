import math

def main():
    T = int(input())

    for i in range(0, T):
        w, h, x0, y0 = list(map(int, input().split()))
        magia, N, cx, cy = input().split()
        N = int(N)
        cx = int(cx)
        cy = int(cy)
        inimigo = [[i for i in range(x0, x0+w)], [j for j in range(y0, y0+w)]]
        aliado = [math.sin(math.radians(k)) for k in range(0, 360 + 1)]



        #if i >= x0 and i <= x0 + w and i >= y0 and i <= y0 + h:
            #Tem a possibilidade do poder ser maior q a area dos inimigos?


if __name__ == '__main__':
    main()
