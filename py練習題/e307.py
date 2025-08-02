from sys import stdin

s=stdin.readline()
spa=0
fs=''
for ch in s:
    if ch==' ':
        spa+=1
    else:
        if spa%2==0:
            spa=0
            fs+=ch
        else:
            spa=0
            fs+=' '+ch
print(fs)