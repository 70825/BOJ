n = int(input())
D = []
for i in range(n):
    s,c,l = map(int,input().split())
    D.append([i+1,s,-c,-l])
D = sorted(D, key = lambda a: [a[1],a[2],a[3]], reverse=True)
print(D[0][0])