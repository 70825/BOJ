M=str(input());k=0;N=int(input());Z=[];r=0
for i in range(8):
    if M[i] != '*':k+=1
for i in range(N):
    B=str(input());o=0
    for j in range(8):
        if B[j]==M[j]:o+=1
    if o==k:
        Z.append(B)
        r+=1
print(r)
for i in range(len(Z)):
    print(Z[i])