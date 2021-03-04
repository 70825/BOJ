for i in range(int(input())):
    S=str(input())
    k=0
    Upper=0
    Lower=0
    num=0
    non=0
    con=0
    NON=['!','@','#','$','%','^','&','*','.',',',';','/','?']
    CON=[]
    NUM=[]
    pel=0
    a='password';A=0
    ar=a[::-1];Ar=0
    b='virginia';B=0
    br=b[::-1];Br=0
    c='cavalier';C=0
    cr=c[::-1];Cr=0
    d='code';D=0
    dr=d[::-1];Dr=0
    if 9<=len(S)<=20:
        k=1
        for j in range(len(S)):
            if 65<=ord(S[j])<=90:Upper+=1
            if 97<=ord(S[j])<=122:Lower+=1
            if 48<=ord(S[j])<=57:num+=1;NUM.append(S[j])
            if S[j] in NON:non+=1
            memo=S[j].lower()
            if A<8:
                if a[A]==memo:A+=1
            if B<8:
                if b[B]==memo:B+=1
            if C<8:
                if c[C]==memo:C+=1
            if D<4:
                if d[D]==memo:D+=1
            if Ar<8:
                if ar[Ar]==memo:Ar+=1
            if Br<8:
                if br[Br]==memo:Br+=1
            if Cr<8:
                if cr[Cr]==memo:Cr+=1
            if Dr<8:
                if dr[Dr]==memo:Dr+=1
            CON.append(S[j].lower())
            if len(CON)==3:
                if CON[0]==CON[1]==CON[2]:con+=1
                CON=[]
    for j in range(len(NUM)//2):
        if NUM[j]==NUM[len(NUM)-1-j]:pel+=1
    if k==1 and Upper>=2 and Lower>=2 and num>=1 and non>=2 and con==0 and pel==0 and A!=8 and B!=8 and C!=8 and D!=4:
        print('Valid Password')
    else:
        print('Invalid Password')