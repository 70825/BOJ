A,B,C=map(str,input().split())
if B=='AND':
    if A=='true':
        if C=='true':print('true')
        else:print('false')
    elif A=='false':
        if C=='false':print('false')
        else:print('false')
elif B=='OR':
    if A=='true':
        if C=='true':print('true')
        else:print('true')
    elif A=='false':
        if C=='false':print('false')
        else:print('true')