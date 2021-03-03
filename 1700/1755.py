A=['zero','one','two','three','four','five','six','seven','eight','nine']
B={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
N,M=map(int,input().split())
memo=[]
for i in range(N,M+1):
    if i<10:memo.append(A[i])
    else:memo.append(A[i//10]+' '+A[i%10])
memo.sort()
if (M-N+1)%10==0:k=0
else:k=1
for i in range(len(memo)//10+k):
    if i == len(memo)//10+k-1:
        for j in range(len(memo)%10):
            num=memo[10*i+j].split(' ')
            if len(num)==1:print(B[num[0]],end=" ")
            else:print(B[num[0]]+B[num[1]],end=" ")
    else:
        for j in range(10):
            num=memo[10*i+j].split(' ')
            if len(num)==1:print(B[num[0]],end=" ")
            else:print(B[num[0]]+B[num[1]],end=" ")
        print("")