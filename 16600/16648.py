t,p=map(int,input().split())
if p>=20:
    x=t/(100-p)
    ans=x*(p-20)+40*x
    print(ans)
else:
    eco=20-p
    x=t/(eco*2+80)
    ans=p*2*x
    print(ans)