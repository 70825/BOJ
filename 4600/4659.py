while 1:
    S=str(input())
    if S=='end':break
    mo=0;ja=0;err=0
    for i in range(len(S)):
        if S[i] in 'aeiou':mo+=1
        else:ja+=1
    if mo==0:err+=1
    mo_cont=0;ja_cont=0
    for i in range(len(S)):
        if S[i] in 'aeiou':ja_cont=0;mo_cont+=1
        else:mo_cont=0;ja_cont+=1
        if ja_cont>=3 or mo_cont>=3:err+=1
    for i in range(1,len(S)):
        if S[i]==S[i-1] and S[i] not in 'eo':err+=1
    if 'eee' in S or 'ooo' in S:err+=1
    if err==0:
        print('<{}> is acceptable.'.format(S))
    else:
        print('<{}> is not acceptable.'.format(S))