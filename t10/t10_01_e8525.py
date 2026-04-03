"""
3
4 -2 5
1 -4 -12
0 1 -3
"""

n = int(input())
matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split()])

c = 0
s = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] < 0 and matrix[i][j] % 2 == 0:
            c += 1
            s += matrix[i][j]

print(c, s)
