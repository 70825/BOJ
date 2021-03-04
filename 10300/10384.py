for i in range(int(input())):
    S=input().upper();a=[0]*26
    for j in range(len(S)):
        if 0<=ord(S[j])-65<=25:a[ord(S[j])-65]+=1
    print('Case '+str(i+1)+':',end=" ")
    if min(a)==3:print('Triple pangram!!!')
    elif min(a)==2:print('Double pangram!!')
    elif min(a)==1:print('Pangram!')
    elif min(a)==0:print('Not a pangram')