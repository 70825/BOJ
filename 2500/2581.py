D=[]
A=int(input())
B=int(input())
def prime(n):
    if n<2:return 1
    if n in (2,3):return 0
    if n%2 is 0 or n%3 is 0:return 1
    if n<9:return 0
    k,l=5,n**0.5
    while k<=l:
        if n%k is 0 or n%(k+2) is 0:return 1
        k+=6
    return 0
for i in range(A,B+1):
    if prime(i)==0:D.append(i)
if len(D)==0:print(-1)
else:print(sum(D));print(min(D))