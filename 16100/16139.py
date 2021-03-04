input=__import__('sys').stdin.readline
k=[*input().strip()]
n=int(input())
pSum=[[0]*26 for _ in range(len(k)+1)]
for i in range(len(k)):
    for j in range(26):
        pSum[i+1][j]=pSum[i][j]
    pSum[i+1][ord(k[i])-97]+=1
for i in range(n):
    a,b,c=input().split()
    print(pSum[int(c)+1][ord(a)-97]-pSum[int(b)][ord(a)-97])