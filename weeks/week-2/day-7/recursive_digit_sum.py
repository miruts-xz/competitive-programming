# Method implements recursive digit sum hackerrank challenge at @https://hackerrank.com/challenges/recursive-digit-sum
def superDigit(n, k):
    if len(n) == 1:
        return int(n) * k
    new_n = 0
    for c in n:
        new_n += int(c)
    return superDigit(str(new_n * k), 1)
