s=["dc", "ba"]
fs1=[]
for chars in s:
    c=list(chars)
    c.sort()
    fs1.append("".join(c))
print(fs1)
# s="".join(fs1)