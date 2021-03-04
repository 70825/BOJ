s,k,h=map(int,input().split())
if s+k+h>99:print('OK')
else:
    Min=min(s,k,h)
    print('Soongsil') if s==Min else print('Korea') if k==Min else print('Hanyang')