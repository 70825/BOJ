n=int(input())
s=[[*map(int,input().split())] for _ in range(n)]
def Z(p,A,B):
    if p==n:
        if len(A)!=n//2 or len(B)!=n//2:return -1
        t1,t2=0,0
        for i in range(n//2):
            for j in range(n//2):
                if i==j:continue
                t1+=s[A[i]][A[j]]
                t2+=s[B[i]][B[j]]
        k=abs(t1-t2)
        return k
    if len(A)>n//2 or len(B)>n//2:return -1
    ans=-1
    t1=Z(p+1,A+[p],B)
    if ans==-1 or (t1!=-1 and ans>t1):ans=t1
    t2=Z(p+1,A,B+[p])
    if ans==-1 or (t2!=-1 and ans>t2):ans=t2
    return ans
print(Z(0,[],[]))