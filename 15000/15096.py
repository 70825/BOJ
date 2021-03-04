n=int(input())
D=[*map(int,input().split())]
a,b=0,0
for i in range(n):
    if D[i]>=0:a+=D[i];b+=1
print(a/b)