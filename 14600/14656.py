T=int(input())
A=input().split();k=0
for i in range(len(A)):
    if i+1!=int(A[i]):k+=1
print(k)