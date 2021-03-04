T=int(input());k=0
D=['']*9999
for i in range(T):
    A,B=map(int,input().split())
    for j in range(A-1,B-1):
        if D[j]!='a':D[j]='a'
for i in range(9999):
    if D[i]=='a':k+=1
print(k)