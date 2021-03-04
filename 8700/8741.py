k=int(input())
s=2**k-1
a=s*(s+1)//2
b=str(bin(a))
for i in range(2,len(b)):
    print(b[i],end="")