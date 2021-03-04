a,b,c=map(int,input().split(':'))
d,e,f=map(int,input().split(':'))
if c>f:f+=60;e-=1
if b>e:e+=60;d-=1
if a>d:d+=24
print((d-a)*3600+(e-b)*60+(f-c))