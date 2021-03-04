Month=[31,28,31,30,31,30,31,31,30,31,30,31]
Month1=[31,29,31,30,31,30,31,31,30,31,30,31]
P,N=input().split()
Y,M,D=map(int,P.split('-'))
N=int(N)+(D-2);D=1
while N!=0:
    if Y%4==0 and (Y%100!=0 or Y%400==0):
        if N>=Month1[M-1]:N-=Month1[M-1];M+=1
        else:D+=N;N=0
    else:
        if N>=Month[M-1]:N-=Month[M-1];M+=1
        else:D+=N;N=0
    if M==13:M=1;Y+=1
if M<10:M='0'+str(M)
if D<10:D='0'+str(D)
print("{}-{}-{}".format(Y,M,D))