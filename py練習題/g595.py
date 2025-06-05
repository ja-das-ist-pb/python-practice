n=int(input())
h=list(map(int, input().split()))
tot=0
for i in range(n):
    if h[i]==0:
        if 0<i<n-1:
            tot+=min(h[i-1], h[i+1])
        elif i==0:
            tot+=h[1]
        elif i==n-1:
            tot+=h[n-2]
print(tot)