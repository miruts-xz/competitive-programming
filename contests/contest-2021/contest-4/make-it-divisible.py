t = int(input())
from collections import defaultdict, deque
from math import inf
nums = [int(input()) for _ in range(t)]

def make_it_divisible():
    def compute(num):
        string = str(num)
        size = len(string)
        zeros = string.count('0')
        ans = size-zeros
        indices = {}
        for look in ['5', '0']:
            try:
                indices[look] = str(num).rindex(look)
            except:
                pass
        r5 = len(string) if '5' not in indices else indices['5']
        r0 = len(string) if '0' not in indices else indices['0']
        if '5' in indices:
            for look in ['2', '7']:
                try:
                    ans = min(ans, size - string.rindex(look, 0, r5)-2)
                except:
                    pass
        if '0' in indices:
            for look in ['0', '5']:
                try:
                    ans = min(ans, size - string.rindex(look, 0, r0)-2)
                except:
                    pass
        return ans
    for n in nums:
        print(compute(n))
make_it_divisible()
