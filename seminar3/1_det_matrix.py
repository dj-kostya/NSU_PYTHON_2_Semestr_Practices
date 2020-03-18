# Matrix Determinant
# Create a function that returns the determinant of a given square matrix.
import json
import os

INPUT_MATRIX = 'Matrix1.json'


def load_matrix() -> list:
    if not os.path.exists(INPUT_MATRIX):
        raise FileNotFoundError(f'Not found {INPUT_MATRIX}')
    with open(INPUT_MATRIX, 'r') as f:
        return json.load(f)


def is_valid_matrix(matrix: list):
    row_len = len(matrix)
    if row_len < 1:
        raise ValueError('Not a valid matrix')
    for row in matrix:
        if not isinstance(row, list):
            raise ValueError('Not a matrix')
        if row_len != len(row):
            raise ValueError('Not a square matrix')
        for column in row:
            if not isinstance(column, int) and not isinstance(column, float):
                raise ValueError('Not a matrix of numbers')


def det(matrix: list) -> int:
    is_valid_matrix(matrix)
    matrix_size = len(matrix)
    if matrix_size == 1:
        return matrix[0][0]
    if matrix_size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    determinant = 0
    for column in range(matrix_size):
        new_matrix = []
        for row_id, row in enumerate(matrix[1:]):
            new_matrix.append(row[:column] + row[column + 1:])
        matrix_det = ((-1) ** column) * det(new_matrix) * matrix[0][column]
        determinant += matrix_det
    return determinant


def pprint_matrix(matrix: list):
    for row in matrix:
        for item in row:
            print(item, end=' ')
        print()


if __name__ == '__main__':
    matrix = load_matrix()
    pprint_matrix(matrix)
    print(f'Determinant = {det(matrix)}')
