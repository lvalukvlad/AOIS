class BinaryConverter:

    @staticmethod
    def convert_to_binary(number: int, bit_length: int) -> list:
        if number < 0:
            raise ValueError("Число не может быть отрицательным")
        if number >= (1 << bit_length):
            raise ValueError(f"Число {number} требует больше чем {bit_length} бит")

        return [int(bit) for bit in format(number, f'0{bit_length}b')]


def convert_to_binary(number: int, bit_length: int) -> list:
    return BinaryConverter.convert_to_binary(number, bit_length)