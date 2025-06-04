n=int(input())

for i in range(n):
    time=list(map(int, input().split()))
    dt=0
    if time[3]>=time[1]:
        dt+=time[3]-time[1]
    else:
        dt+=time[3]+60-time[1]
        time[2]-=1
    dt+=60*(time[2]-time[0])
    
    if dt>=time[4]:
        print("Yes")
    else:
        print("No")