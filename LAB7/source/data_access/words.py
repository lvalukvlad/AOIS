from typing import List


def get_diagonal_word(matrix: List[List[int]], word_idx: int) -> List[int]:
    WORD_SIZE = 16
    bit_sequence = []

    for bit_pos in range(WORD_SIZE):
        target_row = (word_idx + bit_pos) % WORD_SIZE
        bit_sequence.append(matrix[target_row][word_idx])

    return bit_sequence