D=''
while 1:
    try:
        S=str(input())
        D+=S
    except EOFError:break
D=[*map(int,D.split(','))]
print(sum(D))