n=int(input())
for _ in range(n):
    # try:
    s=input()
    s=list(s.strip())
    stack=[]
    times=0
        
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if stack:
                 stack.pop(-1)
                 times+=1
    if stack: times=0
    print(times)