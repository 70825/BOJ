N=int(input())
def A(N):
 d=0;s=4
 while d!=N:s=int((s**(0.5)*2-1)**2);d+=1
 return s
print(A(N))