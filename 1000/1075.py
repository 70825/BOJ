N=int(input())
F=int(input())
n=str(N)[:len(str(N))-2:]
for i in range(100):
    if len(str(i))==1:k='0'+str(i)
    else:k=str(i)
    ans=int(n+k)
    if ans%F==0:print(k);break