def Prime(n):
    check=[0]*(n+1)
    for i in range(2, n+1):
        if not check[i]:
            D.append(i)
            j=i+i
            while j<=n:check[j]=1;j+=i

input=__import__('sys').stdin.readline
n=int(input())
D=[]
Prime(n)
res,Sum,lo,hi=0,0,0,0
while 1:
    if Sum>=n: Sum-=D[lo]; lo+=1
    elif hi==len(D):break
    else:Sum+=D[hi]; hi+=1;
    if Sum==n:res+=1
print(res)