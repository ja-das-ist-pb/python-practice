ans, a=map(int, input().split())
if a!=ans: print(f"{min(a, ans-a)}+{max(a, ans-a)}={ans}")
else: print(f"3+{a-3}={ans}")