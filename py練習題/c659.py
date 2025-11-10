from sys import stdin

def input(): return stdin.readline()

s=list(map(str, input().split()))
conj=' ' +s[0]+' '
s.pop(0)
print(conj.join(s))