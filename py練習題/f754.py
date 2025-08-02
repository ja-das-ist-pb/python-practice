import sys
def input():
    return sys.stdin.readline().strip()
n=int(input())
for j in range(n):
    m, k=map(int, input().split())
    ave=int(m/k)
    print(f'Case {j+1} :')
    for i in range(k-1):
        print(f"第{i+1}位 : 拿{ave}元並說DD! BAD!")
    print(f'第{k}位 : 拿{m-ave*(k-1)}元並說DD! BAD!')