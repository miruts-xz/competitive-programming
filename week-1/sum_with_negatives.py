from typing import List

import utils as util


def subtraction(left: str, right: str):
    right = '0' * (len(left) - len(right)) + right if len(left) > len(right) else right
    if int(left) < int(right):
        return '-' + subtraction(right, left)
    sub_results: List[str] = []
    for i in range(len(left) - 1, -1, -1):
        # borrow if left less right
        left_opd = int(left[i])
        right_opd = int(right[i])
        if left_opd < right_opd:
            j = i - 1
            while not int(left[j]) > 0:
                left = left[:j] + '9' + left[j + 1:]
                j -= 1
            left = left[:j] + str(int(left[j]) - 1) + left[j + 1:]
            d = str(left_opd + 10 - right_opd)
            sub_results.append(d)
        else:
            sub_results.append(str(left_opd - right_opd))
    sub_results.reverse()
    return "".join(sub_results)


def sum_with_negatives(op1, op2):
    if op1[0] == "-" and op2[0] == "-":
        result = util.add_string_num(op1.strip('-'), op2.strip('-'))
        return '-' + str(result)
    elif op1[0] == "-" and op2[0] != "-":
        return subtraction(op2, op1.strip('-'))
    elif op2[0] == '-' and op1[0] != '-':
        return subtraction(op1, op2.strip('-'))
    return util.add_string_num(op1, op2)


print(sum_with_negatives("-123666666666664", '410000000000000000000321'))
