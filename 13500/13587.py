n=input()
k=''
for i in range(len(n)):
    if n[i] in 'aeiou':k+=n[i]
for i in range(len(k)//2):
    if k[i]!=k[len(k)-1-i]:print('N');exit()
print('S')