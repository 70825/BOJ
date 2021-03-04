S=input()[::-1]
ans=''
for i in range(len(S)//3):
    ans+=S[3*i]+S[3*i+1]+S[3*i+2]
    ans+=','
if len(S)%3==2:ans+=S[len(S)-2]+S[len(S)-1];ans=ans[::-1]
elif len(S)%3==1:ans+=S[len(S)-1];ans=ans[::-1]
else:ans=ans[len(ans)-2::-1]
print(ans)