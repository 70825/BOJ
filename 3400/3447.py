while 1:
    try:
        n=[*input()]
        q=[]
        for i in range(len(n)):
            q.append(n[i])
            if q[-1]=='G' and len(q)>=3:
                if q[-3]+q[-2]+q[-1]=='BUG':
                    for j in range(3):
                        q.pop()
        print(''.join(q))
    except EOFError:break