A=[*map(int,input().split())]
B=[*map(int,input().split())]
ans=0;d=0
for i in range(6):
    for j in range(6):
        if A[i]>B[j]:ans+=1
        elif A[i]==B[j]:d+=1
print('{0:.5f}'.format(ans/(36-d)))