T=int(input())
def Z(a):
 C=['a']*len(a)
 for i in range(len(a)):C[i] = a[i]
 a=0
 for i in range(len(C)):a += int(C[i])*10**i
 return a
for i in range(T):A,B=map(str,input().split());K=str(Z(A)+Z(B));print(Z(K))