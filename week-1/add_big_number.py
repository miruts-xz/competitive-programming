import utils as util
import timer


def add_big_number(op1: str, op2: str, *, radix: int = 10) -> str:
    """
    # Defines a function for addition of huge numbers

    :param op1: Operand 1
    :param op2: Operand 2
    :param radix Radix of input operands
    :return: Addition of operands
    """

    # Convert numbers to string
    op1_str = util.power_to_std(op1, radix=radix)
    op2_str = util.power_to_std(op2, radix=radix)

    return util.add_string_num(op2_str, op1_str, radix=radix)


# Test addition algorithm with arbitrary inputs
if __name__ == '__main__':
    time_lapse = timer.Timer()
    result = add_big_number('20^2000', '111^100')
    duration = time_lapse.stop()
    print(f'operation took {duration.seconds} seconds, {duration.microseconds} microseconds', result, sep='\n')
