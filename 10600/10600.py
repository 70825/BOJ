D=[[255,255,255],[192,192,192],[128,128,128],[0,0,0],[255,0,0],[128,0,0],[255,255,0],[128,128,0],[0,255,0],[0,128,0],[0,255,255],[0,128,128],[0,0,255],[0,0,128],[255,0,255],[128,0,128]]
C=['White','Silver','Gray','Black','Red','Maroon','Yellow','Olive','Lime','Green','Aqua','Teal','Blue','Navy','Fuchsia','Purple']
while 1:
    B=[0]*16
    a,b,c=map(int,input().split())
    if a==b==c==-1:break
    for i in range(16):
        B[i]=(D[i][0]-a)**2+(D[i][1]-b)**2+(D[i][2]-c)**2
    for i in range(16):
        if min(B)==B[i]:print(C[i]);break