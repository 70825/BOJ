k=0
while 1:
    try:
        S=str(input())
        k+=1
    except EOFError:break
print(k)