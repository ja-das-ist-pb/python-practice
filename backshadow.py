n=int(input())
a=list(map(int, input().split()))
s=sorted(a)
delta=[s[i+1]-s[i] for i in range (n-1)]
if a.index(s[(delta.index(min(delta)))])>a.index(s[(delta.index(min(delta)))+1]): print(s[(delta.index(min(delta)))+1], s[(delta.index(min(delta)))])
else: print(s[(delta.index(min(delta)))], s[(delta.index(min(delta)))+2])