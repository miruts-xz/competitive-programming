import timer
import utils as util


# Defines a function that multiplies numbers in range [-10 ^ 1000000, 10^1000000]
def multiply_big_number(op1: str, op2: str, *, radix: int = 10) -> str:
    """
    Defines a function for multiplication of huge numbers

    :param op1: Operand 1
    :param op2: Operand 2
    :param radix: Radix of operands
    :return: Multiplication of operands
    """

    # Convert numbers to string
    op1_str = util.power_to_std(op1, radix=radix)
    op2_str = util.power_to_std(op2, radix=radix)

    return util.multiply_string_num(op1_str, op2_str, radix=radix)


# Test huge number multiplication algorithm with arbitrary inputs
if __name__ == '__main__':
    time_lapse = timer.Timer()
    result = multiply_big_number('10^10000', '2^1000')
    duration = time_lapse.stop()
    print(f'operation took {duration.seconds} seconds', result, sep='\n')
