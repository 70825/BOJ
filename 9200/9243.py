n=int(input());k=0
S=input()
D=input()
for i in range(len(S)):
    if S[i]!=D[i]:k+=1
if n%2==1:
    if k==len(S):print('Deletion succeeded')
    else:print('Deletion failed')
else:
    if k==0:print('Deletion succeeded')
    else:print('Deletion failed')