def gcd(a,b):
    mod = a%b
    while mod>0:a=b;b=mod;mod=a%b
    return b
a,b=map(int,input().split())
print('1'*gcd(a,b))