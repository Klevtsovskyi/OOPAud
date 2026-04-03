n = int(input())

s = 0
p = 1
while n > 0:
    d = n % 10
    s += d
    p *= d
    n //= 10

print(f"{p / s:.3f}")
