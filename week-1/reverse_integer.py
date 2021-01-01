def reverse_integer(self, x: int) -> int:
    num = abs(x)
    val = 0
    counter = len(str(num)) - 1
    while num > 0:
        temp = num % 10
        val += temp * 10 ** counter
        num = num // 10
        counter -= 1
    if x < 0:
        val *= -1
    return val

# reverse(120)
