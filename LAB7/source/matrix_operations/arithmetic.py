from typing import List


def binary_sum(operand_a: List[int], operand_b: List[int]) -> List[int]:
    sum_result = [0] * 5
    carry_flag = 0
    for bit_position in range(3, -1, -1):
        bit_sum = operand_a[bit_position] + operand_b[bit_position] + carry_flag
        sum_result[bit_position + 1] = bit_sum % 2
        carry_flag = bit_sum // 2

    sum_result[0] = carry_flag
    return sum_result


def perform_arithmetic(matrix_data: List[List[int]], key_value: List[int]) -> List[List[int]]:
    V_FIELD_LEN = 3
    A_FIELD_LEN = 4
    B_FIELD_LEN = 4
    S_FIELD_LEN = 5

    matching_columns = []
    for col_idx in range(len(matrix_data[0])):
        is_match = True
        for bit_pos in range(len(key_value)):
            if matrix_data[bit_pos][col_idx] != key_value[bit_pos]:
                is_match = False
                break
        if is_match:
            matching_columns.append(col_idx)

    for col_idx in matching_columns:
        a_field = [matrix_data[bit_pos][col_idx]
                   for bit_pos in range(V_FIELD_LEN, V_FIELD_LEN + A_FIELD_LEN)]

        b_field = [matrix_data[bit_pos][col_idx]
                   for bit_pos in range(V_FIELD_LEN + A_FIELD_LEN,
                                        V_FIELD_LEN + A_FIELD_LEN + B_FIELD_LEN)]

        sum_result = binary_sum(a_field, b_field)
        for bit_pos in range(S_FIELD_LEN):
            matrix_data[V_FIELD_LEN + A_FIELD_LEN + B_FIELD_LEN + bit_pos][col_idx] = sum_result[bit_pos]

    return matrix_data