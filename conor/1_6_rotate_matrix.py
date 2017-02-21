from copy import deepcopy


def rotate90(m):
    temp = deepcopy(m)
    # iterate over rows
    col = len(m)-1
    for row in m:
        for i in range(len(row)):
            temp[i][col] = row[i]
        col -= 1
    return temp

if __name__ == "__main__":
    arr = [[i for i in range(j, j+3)] for j in range(0, 9, 3)]
    print(arr)
    print(rotate90(arr))






