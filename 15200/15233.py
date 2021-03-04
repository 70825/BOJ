N,M,L=map(int,input().split())
A=input().split();a=0
B=input().split();b=0
C=input().split()
for i in range(len(C)):
    if C[i] in A:a+=1
    else: b+=1
if a==b:print('TIE')
elif a>b:print('A')
else:print('B')