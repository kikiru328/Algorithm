def solution(arr1, arr2):
    # 두 행렬을 받아서
    arr1_row: int = len(arr1)
    arr1_column: int = len(arr1[0])

    # arr2_row: int = len(arr2)
    arr2_column: int = len(arr2[0])

    ret= [[0] * arr2_column for _ in range(arr1_row)]

    for row in range(arr1_row):
        for column in range(arr2_column):
            for k in range(arr1_column):
                ret[row][column] += arr1[row][k] * arr2[k][column]
    return ret