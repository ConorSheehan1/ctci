# find indexes where 0 occurs, then set rows and columns to 0
# otherwise entire matrix will be set to 0 if 0 is in any position
def zero_indexes(mat):
    indexes = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 0:
                indexes.append([i,j])
    return indexes


def set_zero(mat):
    indexes = zero_indexes(mat)
    for sublist in indexes:
        # set row to all 0s
        mat[sublist[0]] = [0]*len(mat)
        # set column to 0s
        for row in mat:
            row[sublist[1]] = 0
    # no need to return matrix, modify in place


def print_matrix(mat):
    for row in mat:
        print(row)
    print()

matrix = [[0, 1, 2], [1, 1, 3], [1, 0, 5]]
print_matrix(matrix)
set_zero(matrix)
print_matrix(matrix)
