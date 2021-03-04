import sys
for i in range(int(input())):
    s=''
    OP,rD,rA,rB=map(str,sys.stdin.readline().split())
    op=OP
    A=['ADD','SUB','MOV','AND','OR','NOT','MULT','LSFTL','LSFTR','ASFTR','RL','RR']
    B=['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
    if op in A:
        for j in range(12):
            if op==A[j]:s+=B[j];break
        s+='0'
    else:
        op=op.replace('C','')
        for j in range(12):
            if op==A[j]:s+=B[j];break
        s+='1'
    s+='0'
    D=['000','001','010','011','100','101','110','111']
    s+=D[int(rD)]
    if op=='NOT' or op=='MOV':s+='000'
    else:s+=D[int(rA)]
    if OP in A:s+=D[int(rB)]+'0'
    else:s+=B[int(rB)]
    print(s)