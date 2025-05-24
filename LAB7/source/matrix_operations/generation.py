from typing import List
import random

def create_binary_grid(size_x=16, size_y=16) -> List[List[int]]:
    return [
        [random.getrandbits(1) for _ in range(size_y)]
        for _ in range(size_x)
    ]

def display_grid(data: List[List[int]], bits_per_row=16) -> None:
    for idx, row in enumerate(data):
        row_num = f"{idx:2d}: "
        bits_str = ' '.join(str(bit) for bit in row[:bits_per_row])
        print(row_num + bits_str)