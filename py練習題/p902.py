s=list(input())
k=int(input())
asciis=[ord("a") for a in s]
A=ord("A")
a=ord("a")
Z=ord("Z")
z=ord("z")
for i in range(len(s)):
    if asciis[i]<=Z and asciis[i]+k>Z:
        asciis=A+(26%(k-(Z-asciis[i])-1))
    elif asciis[i]<=z and asciis[i]+k>z:
        asciis=a+(26%(k-(z-asciis[i])-1))
    elif asciis[i]>z:
        asciis[i]=asciis[i]
    asciis[i]+=k
print("".join(chr(i) for i in asciis))