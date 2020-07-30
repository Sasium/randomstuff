
def matrix_reader(a, b):
    print(b)
    matrix_parameters = a.split()
    return [input().split() for _ in range(int(matrix_parameters[0]))]


def main_transpose(a):
    return [[x[i] for x in a] for i in range(len(a[0]))]


def side_transpose(a):
    return [[x[i] for x in a[::-1]] for i in range(len(a[0]) - 1, -1, -1)]


def vertical_transpose(a):
    return [x[::-1] for x in a]


def horizontal_transpose(a):
    return [[x for x in a[i]] for i in range(len(a) - 1, -1, -1)]


def multiply(a, c):
    return [[c * float(x) for x in a[y]]
            for y in range(len(a))]


def addition(a, b):
    result = [[0 for x in range(len(a[0]))] for y in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            result[i][j] = float(a[i][j]) + float(b[i][j])
    return result


def multiply_matrices(a, b):
    result = [[0 for x in range(len(b[0]))] for y in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += float(a[i][k]) * float(b[k][j])
    return result


def determinant(a):
    if len(a) == 1:
        return float(a[0][0])
    if len(a) == 2:
        return float(a[0][0]) * float(a[1][1])\
               - float(a[0][1]) * float(a[1][0])
    if len(a) == 3:
        return float(a[0][0]) * float(a[1][1]) * float(a[2][2])\
               + float(a[0][1]) * float(a[1][2]) * float(a[2][0])\
               + float(a[0][2]) * float(a[1][0]) * float(a[2][1])\
               - float(a[0][2]) * float(a[1][1]) * float(a[2][0])\
               - float(a[0][0]) * float(a[1][2]) * float(a[2][1])\
               - float(a[0][1]) * float(a[1][0]) * float(a[2][2])
    s = 0
    for i in range(len(a)):
        minor = [row[:i] + row[i + 1:] for row in (a[:0] + a[0 + 1:])]
        s += float(a[0][i]) * (-1) ** (2 + i) * determinant(minor)
    return s


def minor_calc(a, b, c):
    return [row[:b] + row[b + 1:] for row in (a[:c] + a[c + 1:])]


def inverse(a):
    det_inverse = determinant(a)
    if det_inverse == 0:
        return "This matrix doesn't have an inverse."
    cofactor_matrix = [[0 for x in range(len(a[0]))] for y in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a)):
            minor = [row[:j] + row[j + 1:] for row in (a[:i] + a[i + 1:])]
            cofactor_matrix[i][j] = (-1) ** (2 + i + j) * determinant(minor)
    transpose_inverse = main_transpose(cofactor_matrix)
    inversed_matrix = multiply(transpose_inverse, 1 / det_inverse)
    for i in range(len(a)):
        for j in range(len(a[0])):
            inversed_matrix[i][j] = round(inversed_matrix[i][j], 3)
            if inversed_matrix[i][j] == 0.0:
                inversed_matrix[i][j] = 0
    return inversed_matrix


while True:
    option = int(input('''1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit
Your choice:'''))
    if option == 1 or option == 3:
        matrix_1 = matrix_reader(input("Enter size of first matrix:"),
                                 "Enter first matrix:")
        matrix_2 = matrix_reader(input("Enter size of second matrix:"),
                                 "Enter second matrix:")
        if option == 1:
            result_matrix = addition(matrix_1, matrix_2)
        else:
            result_matrix = multiply_matrices(matrix_1, matrix_2)
    elif option == 2:
        matrix = matrix_reader(input("Enter size of matrix:"), "Enter matrix:")
        result_matrix = multiply(matrix,
                                 float(input("Enter constant:")))
    elif option == 4:
        sub_option = int(input('''1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
Your choice:'''))
        matrix = matrix_reader(input("Enter size of matrix:"), "Enter matrix:")
        if sub_option == 1:
            result_matrix = main_transpose(matrix)
        elif sub_option == 2:
            result_matrix = side_transpose(matrix)
        elif sub_option == 3:
            result_matrix = vertical_transpose(matrix)
        else:
            result_matrix = horizontal_transpose(matrix)
    elif option == 5:
        matrix = matrix_reader(input("Enter size of matrix:"), "Enter matrix:")
        det = determinant(matrix)
    elif option == 6:
        matrix = matrix_reader(input("Enter size of matrix:"), "Enter matrix:")
        result_matrix = inverse(matrix)
    else:
        break
    print("The result is:")
    if option == 6 and isinstance(result_matrix, str):
        print(result_matrix)
    elif option != 5:
        col_width = max(len(str(word)) for row in result_matrix for word in row) + 2
        for row in result_matrix:
            print(' '.join(str(word).ljust(col_width) for word in row))
    else:
        print(det)
