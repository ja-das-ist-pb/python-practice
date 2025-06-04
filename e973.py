s=input()
a=[0]*10
for i in s:
    if i=="0":
        a[0]+=1
    elif i=="1":
        a[1]+=1
    elif i=="2":
        a[2]+=1
    elif i=="3":
        a[3]+=1
    elif i=="4":
        a[4]+=1
    elif i=="5":
        a[5]+=1
    elif i=="6":
        a[6]+=1
    elif i=="7":
        a[7]+=1
    elif i=="8":
        a[8]+=1
    elif i=="9":
        a[9]+=1    
count=len(list(filter(lambda x:x>0, a)))

for i in range(count):  
    print(a.index(max(a)), end=' ')
    a[a.index(max(a))]=-1