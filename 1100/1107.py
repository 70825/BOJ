N=int(input())
m=int(input())
if m!=0:M=[*map(int,input().split())]
else:M=[]
ans=abs(N-100)
def possible(k):
    if k==0:
        if k in M:return False
        else:return True
    else:
        while k>0:
            if k%10 in M:return False
            k//=10
        return True
for i in range(1000000):
    if possible(i):
        if ans>abs(N-i)+len(str(i)):
            ans=abs(N-i)+len(str(i))
print(ans)