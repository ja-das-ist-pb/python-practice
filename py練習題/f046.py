w=int(input())
s=input()
t=int(input())
s+=" "*w
t%=len(s)+w-1
if t>=w:
    print(s[t-w:t])
else:
    print(' '*(w-len(s[:t]))+s[:t])