n=int(input())
a=[]*n
a=list(map(int, input().split()))
e=0

for i in range(1,n):
    if a[i]>a[i-1]:
        e+=(a[i]-a[i-1])*3
    else:
        e+=(a[i-1]-a[i])*2
print(e+3*(a[0]-1))