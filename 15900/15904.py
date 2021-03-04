S=str(input())
K=['U','C','P','C'];k=0
for i in range(len(S)):
    if S[i]==K[k]:k+=1
    if k==4:break
if k==4:print('I love UCPC')
else:print('I hate UCPC')