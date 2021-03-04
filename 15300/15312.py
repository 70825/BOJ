D=[3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
A=input()
B=input()
memo=[]
for i in range(len(A)):
    memo.append(D[ord(A[i])-65])
    memo.append(D[ord(B[i])-65])
while len(memo)!=2:
    k=[0]*(len(memo)-1)
    for i in range(len(memo)-1):
        k[i]=memo[i]+memo[i+1]
        if k[i]>=10:k[i]%=10
    memo=k
print(''.join(map(str,memo)))