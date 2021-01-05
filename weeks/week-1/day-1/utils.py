# Converts num from given base to 10
def to_base10(num: int, init_base) -> int:
    index = 0
    result = ""
    input_len = len(str(num))
    while index <= input_len:
        trailing_digit = num % 10
        result = add_string_num(result, multiply_string_num(str(trailing_digit), power_to_std(f'{init_base}^{index}')))
        num //= 10
        index += 1
    return int(result)


# Defines a function that multiplies literal numeric strings
def multiply_string_num(opr1: str, opr2: str, *, radix: int = 10) -> str:
    sub_multiplies = []
    for d2 in range(len(opr2) - 1, -1, -1):
        multiplier = int(opr2[d2], base=radix)
        current = ''
        # current = []
        carry = 0
        for d1 in range(len(opr1) - 1, -1, -1):
            temp_ml = int(opr1[d1], base=radix) * multiplier + carry
            curr = temp_ml % radix
            current = str(curr) + current
            # current.append(str(curr))
            carry = temp_ml // radix
        if carry:
            current = str(carry) + current
            # current.append(str(carry))
        # current.reverse()
        sub_multiplies.append(current)
        # sub_multiplies.append("".join(current))

    # Append trailing zeros based on level
    for i in range(1, len(sub_multiplies)):
        sub_multiplies[i] = sub_multiplies[i] + ('0' * i)

    # Add sub multiples
    result = sub_multiplies.pop()
    while len(sub_multiplies) > 0:
        result = add_string_num(result, sub_multiplies.pop(), radix=radix)
    return result


# Converts power notation to standard notation i.e. 10^10 to 10000000000
def power_to_std(pow_num: str, radix: int = 10) -> str:
    num_split = pow_num.split('^', 2)
    base, power = num_split[0], num_split[1]
    b10_power = int(power, base=radix)
    if radix != 10:
        b10_power = to_base10(int(power, base=radix), init_base=radix)
    if b10_power == 0 or int(base) == 1:
        return '1'
    elif b10_power == 1:
        return base
    if base == 0 and b10_power != 0:
        return '0'

    result = '1'
    for i in range(b10_power):
        result = multiply_string_num(result, base, radix=radix)
    return result


def add_string_num(op1: str, op2: str, *, radix: int = 10) -> str:
    """
    # Defines a function that adds literal numeric string

    :param op1: Operand 1
    :param op2: Operand 2
    :param radix: Radix of input operands
    :return: Summation of operands
    """
    op1_len, op2_len = len(op1), len(op2)

    # Add leading zeros to make operands equivalent in length
    if op1_len >= op2_len:
        op2 = op2.zfill(op1_len)
    else:
        op1 = op1.zfill(op2_len)
    result = ''
    # result = []
    carry = 0
    for i in range(len(op1) - 1, -1, -1):
        temp_ad = int(op1[i], base=radix) + int(op2[i], base=radix) + carry
        curr = temp_ad % radix
        result = str(curr) + result
        # result.append(str(curr))
        carry = temp_ad // radix
    if carry:
        result = str(carry) + result
        # result.append(str(carry))
    # result.reverse()
    return result
    # return "".join(result)
