# rotate a matrix by 90 degrees
# given NxN. Matrix is assumed to be stored as
# multidimensional array.
# cases:
# 0x0, 1x1, NxN

n_matrix = [[1,2,3], [4,5,6], [7,8,9]]

def rotater(matrix, n):
    n -= 1
    rotated = [[None]*3, [None]*3, [None]*3]

    for index, row in enumerate(matrix):
        for elem in row:
            rotated[n][n-index] = elem

    return rotated

print(rotater(n_matrix, 3))
