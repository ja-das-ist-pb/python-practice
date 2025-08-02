n=int(input())
print(" "*(n-1)+"*")
for i in range(2, n+1):
    print(" "*(n-i)+"* "*(i))
for i in range(n//2):
    print(" "*(n-2)+"| |")
print("\\", end="")
for i in range(2*n-3):
    print("_", end="")
print("/", end="")
