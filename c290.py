a=list(input())
print(abs(sum([int(a[i]) for i in range(len(a)) if i %2==0]) - sum([int(a[i]) for i in range(len(a)) if i % 2 ==1])))