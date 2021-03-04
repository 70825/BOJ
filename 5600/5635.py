D=[]
for i in range(int(input())):
    a,b,c,d=map(str,input().split())
    D.append([int(d),int(c),int(b),a])
D.sort()
print(D[len(D)-1][3])
print(D[0][3])