from sys import stdin
from decimal import Decimal, ROUND_HALF_UP

for line in stdin:
    a=Decimal(line.strip())
    a=a.quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)
    if a==Decimal("-0.00"): a=Decimal("0.00")
    print(f"{a:.2f}")