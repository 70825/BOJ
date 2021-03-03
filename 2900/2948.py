day=['Sunday',"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
D,M=map(int,input().split())
if M in [1,10]:print(day[(D+3)%7])
elif M in [2,3,11]:print(day[(D+6)%7])
elif M in [4,7]:print(day[(D+2)%7])
elif M==5:print(day[(D+4)%7])
elif M==6:print(day[D%7])
elif M==8:print(day[(D+5)%7])
else:print(day[(D+1)%7])