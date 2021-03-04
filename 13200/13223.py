h=[0]*2;m=[0]*2;s=[0]*2
for i in range(2):
    h[i],m[i],s[i]=map(int,input().split(':'))
if s[1]-s[0]<0:m[1]-=1;S=60+s[1]-s[0]
else:S=s[1]-s[0]
if m[1]-m[0]<0:h[1]-=1;M=60+m[1]-m[0]
else:M=m[1]-m[0]
if h[1]-h[0]<0:H=24+h[1]-h[0]
else:H=h[1]-h[0]
if H<10:H='0'+str(H)
if M<10:M='0'+str(M)
if S<10:S='0'+str(S)
if H=='00' and M=='00' and S=='00':print('24:00:00')
else:print(str(H)+':'+str(M)+':'+str(S))