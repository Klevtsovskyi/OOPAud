x1, y1, x2, y2, x3, y3 = [float(n) for n in input().split()]
# print(x1, y1, x2, y2, x3, y3)

a = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
b = ((x1 - x3)**2 + (y1 - y3)**2)**0.5
c = ((x3 - x2)**2 + (y3 - y2)**2)**0.5

P = a + b + c

p = P / 2
S = (p * (p - a) * (p - b) * (p - c))**0.5

print(f"{P:.4f} {S:.4f}")
