#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is illegal.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations. Don't get too scared I'm kidding :)


def division(dividend: str, divisor: str) -> tuple:
    """
    Method for large number division

    :param dividend: Dividend of the operation. aka Numerator
    :param divisor: Divisor of the operation. aka Denominator
    :return: Tuple of quotient and remainder i.e. (quotient, remainder)
    """
    ctr = 0
    result = ''
    remainder = "0"
    while ctr < len(dividend):
        curr = dividend[ctr]
        if remainder != "0":
            curr = remainder + dividend[ctr]
        while int(curr) < int(divisor) and ctr < len(dividend) - 1:
            ctr += 1
            curr += dividend[ctr]
            result += '0'
        try:
            quo, remainder = str(int(curr) // int(divisor)), str(int(curr) % int(divisor))
        except ZeroDivisionError:
            return 'NaN', 'NaN'
        result += quo
        ctr += 1
    result = str(int(result))
    return result, remainder


print(division('2175896', '18'))
