right_score=[0]*26
wrong_score=[0]*26
sum=0;solve=0
while True:
    a=input().split()
    if a[0]=='-1':break
    if a[2]=='wrong':
        wrong_score[ord(a[1])-65]+=20
    else:
        right_score[ord(a[1])-65]+=int(a[0])
        solve+=1
for i in range(26):
    if right_score[i]!=0:
        sum+=right_score[i]+wrong_score[i]
print(solve,sum)