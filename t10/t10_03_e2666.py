n = int(input())

matrix = [
    [0 for j in range(n)]
    for i in range(n)
]

for i in range(n - 1):
    for j in range(n - i - 1):
        matrix[i][j] = 2

for i in range(1, n):
    for j in range(n - i, n):
        matrix[i][j] = 1


for row in matrix:
    print(*row, sep="")
