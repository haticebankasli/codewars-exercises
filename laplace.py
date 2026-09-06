def determinant(matrix):
    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    else:
        total = 0

        for col in range(n):
            minor = [row[:col] + row[col+1:] for row in matrix[1:]]

            m = matrix[0][col] * determinant(minor)

            if col % 2 == 0:
                total += m
            else:
                total -= m

        return total