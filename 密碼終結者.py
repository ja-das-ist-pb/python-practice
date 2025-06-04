import random

print("密碼限制: a-z, 0-9")
code=input("請輸入密碼: ")
guess=""
char=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

while guess!=code:
    guess=""
    for i in range(len(code)):
        guess+=random.choice(char)
    if guess!=code:
        print(guess)
print(f'Your code is "{guess}"')
print('菜就多練')