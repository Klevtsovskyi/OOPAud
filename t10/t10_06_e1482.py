def input_matrix():
    n, m = [int(x) for x in input().split()]
    matrix = [
        [int(x) for x in input().split()]
        for _ in range(n)
    ]
    return matrix


def print_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    print(n, m)
    for row in matrix:
        print(*row)


def multiply(A, B):
    n = len(A)
    m = len(B[0])
    C = [
        [0 for j in range(m)]
        for i in range(n)
    ]

    for i in range(n):
        for j in range(m):
            for r in range(len(B)):
                C[i][j] += A[i][r] * B[r][j]
    return C


A = input_matrix()
B = input_matrix()

if len(A[0]) != len(B):
    print(-1)
else:
    C = multiply(A, B)
    print_matrix(C)
