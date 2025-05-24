from typing import List
from source.matrix_operations.generation import display_grid


def extract_circular_word(data: List[int], start_pos: int) -> List[int]:
    WORD_SIZE = 16
    return [data[(start_pos + i) % WORD_SIZE] for i in range(WORD_SIZE)]


def transpose_matrix(grid: List[List[int]]) -> List[List[int]]:
    return [[grid[row][col] for row in range(len(grid))]
            for col in range(len(grid[0]))]


def compare_bit_sequences(seq_a: List[int], seq_b: List[int],
                          compare_pos: int) -> bool:
    for i in range(compare_pos, len(seq_a)):
        if seq_a[i] != seq_b[i]:
            return seq_a[i] > seq_b[i]
    return False


def sort_matrix_columns(grid: List[List[int]]) -> List[List[int]]:
    columns = transpose_matrix(grid)
    n = len(columns)

    for last_unsorted in range(n - 1, 0, -1):
        max_idx = last_unsorted
        for current in range(last_unsorted):
            current_word = extract_circular_word(columns[current], last_unsorted)
            max_word = extract_circular_word(columns[max_idx], last_unsorted)

            if compare_bit_sequences(current_word, max_word, last_unsorted):
                max_idx = current

        if max_idx != last_unsorted:
            columns[last_unsorted], columns[max_idx] = \
                columns[max_idx], columns[last_unsorted]

    return transpose_matrix(columns)


def perform_ordered_selection(matrix: List[List[int]]) -> List[List[int]]:
    print("\nOriginal matrix:")
    display_grid(matrix)

    sorted_matrix = sort_columns_by_diagonal(matrix)

    print("\nSorted matrix:")
    display_grid(sorted_matrix)

    return sorted_matrix