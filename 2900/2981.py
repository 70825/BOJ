n = int(input())
D = sorted([int(input()) for _ in range(n)])
div = []
k = D[-1] - D[0]
for i in range(1,k):
    if k // i < i: break
    if k % i == 0:
        div.append(i)
        if k // i != i: div.append(k//i)
div = sorted(div)[1:]
for i in range(len(div)):
    z = D[0] % div[i]
    flag = True
    for j in range(1,len(D)):
        if D[j] % div[i] != z: flag = False
    if flag: print(div[i], end =' ')