def gcd(a,b):
    mod=a%b
    while mod>0:
        a=b
        b=mod
        mod=a%b
    return b
def lcm(a,b):
    return a*b//gcd(a,b)
a,b=map(int,input().split())
print(gcd(a,b))
print(lcm(a,b))