def string1(s):
    fs=list(s)
    s1=[]
    for i in range(0, len(s), 2):
        s1.append(fs[i]+fs[i+1])
    return s1
def string2(s):
    fs=list(s)
    s21=[]
    s22=[]
    for i in range(len(s)//2):
        s21.append(fs[i])
        s22.append(fs[i+len(s)//2])
    return s21, s22    
s=input()
k=int(input())
com=[int(input()) for _ in range (k)]
s1=[]
s21=[]
s22=[]

for i in range(k):
    
    # print(com[i])
        
    if com[i]==0:
        s1=string1(s)

        # print(s1)
        fs1=[]
        for chars in s1:
            c=list(chars)
            ft=c[1]+c[0]
            fs1.append(ft)
        s="".join(fs1)
    if com[i]==1:
        s1=string1(s)

        # print(s1)
        fs1=[]
        for chars in s1:
            c=list(chars)
            c.sort()
            fs1.append("".join(c))
        s="".join(fs1)
    if com[i]==2:
        s21, s22=string2(s)
        
        # print(s21, s22)

        s21, s22=list(s21), list(s22)
        fakes=[]
        for j in range(len(s)//2):
            fakes.append(s21[j])
            fakes.append(s22[j])
        s="".join(fakes)
    # print(s)
print(s)