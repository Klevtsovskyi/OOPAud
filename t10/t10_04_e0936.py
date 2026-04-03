def determinant(matr):
    return matr[0][0] * matr[1][1] - matr[0][1] * matr[1][0]


a11, a12, b1 = [int(n) for n in input().split()]
a21, a22, b2 = [int(n) for n in input().split()]

d0 = determinant([
    [a11, a12],
    [a21, a22]
])
d1 = determinant([
    [b1, a12],
    [b2, a22]
])
d2 = determinant([
    [a11, b1],
    [a21, b2]
])

x = d1 / d0
y = d2 / d0

print(f"{x:.3f}")
print(f"{y:.3f}")
