from typing import List


def extract_diagonal_column(matrix_data: List[List[int]], column_index: int) -> List[int]:
    MATRIX_SIZE = 16
    result_column = []

    for row_offset in range(MATRIX_SIZE):
        wrapped_col = (column_index + row_offset) % MATRIX_SIZE
        result_column.append(matrix_data[row_offset][wrapped_col])

    return result_column