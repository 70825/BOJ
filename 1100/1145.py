def gcd(a,b):
    mod = a%b
    while mod>0:a=b;b=mod;mod=a%b
    return b
def lcm(a,b):
    return a*b//gcd(a,b)
D=[*map(int,input().split())]
memo=[]
for i in range(3):
    for j in range(i+1,4):
        for k in range(j+1,5):
            memo.append(lcm(lcm(D[i],D[j]),D[k]))
print(min(memo))