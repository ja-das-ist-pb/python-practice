n=int(input())
s=[]
a=[]
ss=["-"]*(n+2)
s.append(ss)
for i in range(n):
    s.append("-")
    sub=input()
    sub+="-"
    s.append(list[sub])
s.append(ss)

print(s)

if n>2:
    for i in range(n+2):        
        a.append(0)
        b=[0]*n
        b.append(0)
        a.append(b)

    for i in range(1, n+1):
        for j in range(1, n+1):
            if s[i][j]=="*":
                a[i][j-1]+=1
                a[i][j+1]+=1
                a[i-1][j]+=1
                a[i+1][j]+=1
                a[i-1][j-1]+=1
                a[i-1][j+1]+=1
                a[i+1][j-1]+=1
                a[i+1][j+1]+=1
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if s[i][j]=="*":
                print(s[i][j], end=" ")
            elif s[i][j]=="-" and a[i][j]==0:
                print(s[i][j], end=" ")
            else:
                print(a[i][j], end=" ")
        print()
else:
    a=[0]*(n*2)    
    for i in range(1, n+1):
        if s[i]=="*":
            a[i-1]+=1
            a[i+1]+=1