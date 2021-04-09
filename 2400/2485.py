def gcd(a,b):
    while b != 0:a,b = b,a%b
    return a

input = __import__('sys').stdin.readline
n = int(input())
D = sorted([int(input()) for i in range(n)])
D = list([D[i]-D[i-1] for i in range(1,n)])
S = list(set(D))
s = 0
for i in range(len(S)-1):
    t = gcd(S[i],S[i+1])
    for j in range(i+2,len(S)):
        t = gcd(t,S[j])
    s = gcd(t,s)
if s == 0:print(0);exit()
ans = 0
for i in range(len(D)):
    ans += D[i]//s - 1
print(ans)