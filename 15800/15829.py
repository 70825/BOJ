N=int(input())
L=input()
s=0
for i in range(N):
    s+=(ord(L[i]) - 96)*31**i
print(s%1234567891)