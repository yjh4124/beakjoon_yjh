
import sys

input = sys.stdin.readline


def getPowMatrix(a_matrix, n, b):
    if b == 1:
        matrix = [[elem % 1000 for elem in row] for row in a_matrix]
        return matrix

    halfPowMatrix = getPowMatrix(a_matrix, n, b // 2)
    if b % 2 == 0:
        return getMulMatrix(
            halfPowMatrix,
            halfPowMatrix,
            n,
        )
    else:
        return getMulMatrix(
            getMulMatrix(
                halfPowMatrix,
                halfPowMatrix,
                n,
            ),
            a_matrix,
            n,
        )


def getMulMatrix(matrix1, matrix2, n):
    mulMatrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                mulMatrix[i][j] += matrix1[i][k] * matrix2[k][j]
            mulMatrix[i][j] %= 1000

    return mulMatrix


n, b = map(int, input().split())

a_matrix = tuple((tuple(map(int, input().split()))) for _ in range(n))
memo = {}

resultMatrix = getPowMatrix(a_matrix, n, b)

for i in resultMatrix:
    print(*i)
