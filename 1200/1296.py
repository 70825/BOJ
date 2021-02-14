m=input()
def z(k):
    w,x,y,z=0,0,0,0
    for j in range(len(k)):
        if k[j]=='L':w+=1
        if k[j]=='O':x+=1
        if k[j]=='V':y+=1
        if k[j]=='E':z+=1
    return w,x,y,z
a,b,c,d=z(m)
D=[]
n=int(input())
for i in range(n):
    D.append(input())
D.sort()
ans=0;an=D[0]
for i in range(n):
    L,O,V,E=z(D[i])
    L+=a;O+=b;V+=c;E+=d
    t=((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E))%100
    if t>ans:ans=t;an=D[i]
print(an)