def read_matrix(filename):
    matrix = []
    f = open(filename)
    for line in f:
        matrix.append([int(x) for x in line.split()])
    f.close()
    return matrix


def write_matrix(filename, matrix):
    f = open(filename, "w")
    for row in matrix:
        print(*row, file=f)
    f.close()


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


A = read_matrix("matrixA.txt")
B = read_matrix("matrixB.txt")
C = multiply(A, B)
write_matrix("matrixC.txt", C)
