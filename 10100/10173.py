while 1:
    A=str(input())
    if A=='EOI':break
    A=A.lower()
    if A.count('nemo')>0:print('Found')
    else:print('Missing')