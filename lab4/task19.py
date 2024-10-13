def transpose(matrix):
    transposed = []
    for i in range(len(matrix[0])):
        new_row = []
        for j in range(len(matrix)):
            new_row.append(matrix[j][i])
        transposed.append(new_row)
    return transposed


if __name__ == "__main__":
    matrix = [
        [1, 2],
        [3, 4]
    ]

    transposed_matrix = transpose(matrix)
    print(transposed_matrix)
