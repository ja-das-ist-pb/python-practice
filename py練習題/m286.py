n, m=map(int, input().split())
if n<m:
    print('真分數', f'{n}/{m}')
elif n%m==0:
    print('整數', n//m)
else:
    print('帶分數', n//m, f'{n%m}/{m}')