while 1:
    A=input()
    if A=='#':break
    memo={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7}
    if len(A)==1:
        print('That music is beautiful.')
    else:
        ans=0
        sub_memo=[2,4,6]
        for i in range(len(A)-1):
            a=memo[A[i]];b=memo[A[i+1]]
            if a>b:b+=7
            if b-a in sub_memo:ans+=1
        if ans==len(A)-1:
            print('That music is beautiful.')
        else:
            print('Ouch! That hurts my ears.')