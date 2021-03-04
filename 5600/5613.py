D=0;A=int(input());D+=A
while 1:
    B=str(input())
    if B=='=':break
    C=int(input())
    if B=='+':D+=C
    elif B=='-':D-=C
    elif B=='*':D*=C
    elif B=='/':D//=C
print(D)