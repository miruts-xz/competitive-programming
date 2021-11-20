def solve(a, b, sequence):
    sequence = [s for s in sequence]
    for _ in range(2):
        for i in range(len(sequence)):
            if sequence[i] != '?':
                if sequence[~i] == '?':
                    sequence[~i] = sequence[i]
                elif sequence[~i] != sequence[i]: return '-1'
        sequence.reverse()
    one_count = sequence.count('1')
    zero_count = sequence.count('0')
    a -= zero_count
    b -= one_count
    ques = sequence.count('?')
    mid = True if len(sequence)%2 and sequence[len(sequence)//2] == '?' else False
    if a < 0 or b < 0 or a + b != ques or (mid and a % 2 == 0 and b % 2 == 0):
        return '-1'
    if a % 2 == 1 or b % 2 == 1:
        if sequence[len(sequence)//2] != '?':
            return '-1'
        sequence[len(sequence)//2] = '0' if a%2 else '1'
        if a%2:
            a -= 1
        else:
            b-= 1
    if a % 2 == 1 or b % 2 == 1:
        return '-1'
    for i in range(len(sequence)):
        if sequence[i] == '?':
            if a > 0:
                sequence[i] = sequence[~i] = '0'
                a -= 2
            else:
                sequence[i] = sequence[~i] = '1'
                b -= 2
    return ''.join(sequence)
    
    
if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        a, b = map(int, input().split())
        ans.append(solve(a, b, input()))
    print(*ans, sep='\n')