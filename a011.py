import string
def isalp(char):
    return "A" <= char <= "Z" or "a" <= char <= "z"

while True:
    try:
        words = 0
        s = input()
        s = list(map(str, s.split()))
        for word in s:
            word = word.strip(string.punctuation)  # <-- 重點修正：對每個 word 清除標點
            notcount = True
            for char in word:
                if not isalp(char):
                    notcount = False
                    break
            if notcount and word != "":
                words += 1
        print(words)
    except EOFError:
        break
