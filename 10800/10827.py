a,b=map(str,input().split())
b=int(b);a=a.split('.');k=len(a[1])
a=int(a[0])*10**k+int(a[1])
N=str(a**b)
if len(N)<=k*b:
    N='0'*(k*b-len(N)+1)+N
x=N[:len(N)-k*b:]
y=N[len(N)-k*b::]
print(x+'.'+y)