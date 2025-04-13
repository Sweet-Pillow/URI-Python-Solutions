A, B = list(map(int, input().split()))

q = 0
r = 0

if(B < 0):
    q = -(A // (-B))
else:
    q = A // B

r = A - (q * B) 

print(f'{q} {r}')