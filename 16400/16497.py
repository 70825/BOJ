D=[]
Book=[0]*31
for i in range(int(input())):
    a,b=map(int,input().split())
    for j in range(a-1,b-1):
        Book[j]+=1
N=int(input())
if max(Book)>N:print(0)
else:print(1)