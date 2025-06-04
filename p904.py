def fourfive(total):
    if total<int(total)+0.5:
        return int(total)
    else:
        return int(total)+1

n=int(input())
a=[0]*n
a=list(map(int, input().split()))
total=sum(a)

if n<=10:
    total=total
elif n<=20:
    total*=0.95
elif n<=40:
    total*=0.9
else:
    total*=0.85
total=fourfive(total)
if total<1200:
    print(int(total))
else:
    print(1200)