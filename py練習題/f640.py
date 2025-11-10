# 𝑓(𝑥) = 2𝑥 – 3
# 𝑔(𝑥, 𝑦) = 2𝑥 + 𝑦 – 7
# ℎ(𝑥, 𝑦, 𝑧) = 3𝑥 – 2𝑦 + 𝑧

def f(s):
    x = 0
    if s[0] == 'f':
        x = f(s[1:])
    elif s[0] == 'g':
        x = g(s[1:])
    elif s[0] == 'h':
        x = h(s[1:])
    else: 
        return x * 2 - 3
def g(s):
    x = 0
    y = 0
    

def h(s): 


s = input()
ans = 0
if s[0] == 'f':
    ans = f(s)
elif s[0] == 'g':
    ans = g(s)
elif s[0] == 'h':
    ans = h(s)
print(ans)