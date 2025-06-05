n=int(input())
a=list(map(int, input().split()))
sa=sorted(a)
for i in sa:
    print(i, end=" ")
print()
rsa=sa[::-1]
print(rsa[0], end=" ")
for i in range(1, len(rsa)):
    if rsa[i]!=rsa[i-1]:
        print(rsa[i], end=" ")