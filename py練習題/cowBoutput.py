import time

s=list(input("給我一串文字，我可以給你很帥的輸入: "))
char=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "]
o=""
for i in range(len(s)):
    if o=="".join(s):
        break
    else:
        for j in range(37):
            time.sleep(0.03)
            if char[j]==s[i]:
                print(o+char[j])
                o+=char[j]
                break
            print(o+char[j])