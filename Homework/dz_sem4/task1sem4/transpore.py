import copy




def transpose(matrix: list):

    result = []
    for l in range(len(matrix[0])):
        result.append(list(0 for i in range(len(matrix))))

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]
            print(result)


    return result