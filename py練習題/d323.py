import sys

def input(): return sys.stdin.readline().strip()

n=int(input())
a=list(map(int, input().split()))
print(" ".join(list(map(str, sorted(a)))))