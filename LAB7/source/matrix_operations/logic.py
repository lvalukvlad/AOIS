from typing import List


def apply_bitwise_xor(bits_a: List[int], bits_b: List[int]) -> List[int]:
    return [bit_a ^ bit_b for bit_a, bit_b in zip(bits_a, bits_b)]


def apply_bitwise_equiv(bits_a: List[int], bits_b: List[int]) -> List[int]:
    return [1 if bit_a == bit_b else 0 for bit_a, bit_b in zip(bits_a, bits_b)]


def apply_bit_inhibit(bits_a: List[int], bits_b: List[int]) -> List[int]:
    return [1 if not bit_a and bit_b else 0 for bit_a, bit_b in zip(bits_a, bits_b)]


def apply_implication(bits_a: List[int], bits_b: List[int]) -> List[int]:
    return [0 if bit_a and not bit_b else 1 for bit_a, bit_b in zip(bits_a, bits_b)]


def execute_logical_ops(operand_a: List[int], operand_b: List[int]) -> dict:
    results = {
        'XOR': apply_bitwise_xor(operand_a, operand_b),
        'Equivalence': apply_bitwise_equiv(operand_a, operand_b),
        'Inhibition': apply_bit_inhibit(operand_a, operand_b),
        'Implication': apply_implication(operand_a, operand_b)
    }

    for op_name, result in results.items():
        print(f'{op_name:12} → {result}')

    return results