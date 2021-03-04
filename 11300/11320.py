T=int(input())
for i in range(T):
 A,B=map(int,input().split());C=A//B;d=0
 for i in range(C):d +=2*i+1
 print(d)