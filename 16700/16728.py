def score(x,y):
    d=(x**2+y**2)**.5
    if d<=10:return 10
    elif 10<d<=30:return 9
    elif 30<d<=50:return 8
    elif 50<d<=70:return 7
    elif 70<d<=90:return 6
    elif 90<d<=110:return 5
    elif 110<d<=130:return 4
    elif 130<d<=150:return 3
    elif 150<d<=170:return 2
    elif 170<d<=190:return 1
    else:return 0
ans=0
for i in range(int(input())):
    a,b=map(int,input().split())
    ans+=score(a,b)
print(ans)