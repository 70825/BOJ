A,B=map(int,input().split())
if A/B==int(A/B):
    print(A//B)
else:
    C=A//B
    A-=C*B
    ans=str(C)+'.'
    m=0
    while m!=1000:
        A=A*10
        C=A//B
        ans+=str(C)
        A-=C*B
        if A==0:break
        m+=1
    print(ans)