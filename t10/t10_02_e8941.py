n, m = [int(x) for x in input().split()]

matrix = [
    [0 for j in range(m)]
    for i in range(n)
]

c = 0
for i in range(n):
    for j in range(m):
        c += 1
        matrix[i][j] = c

for row in matrix:
    print(*row)
