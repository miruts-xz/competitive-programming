def main(strs):
    def valid():
        return  d['a'] > max(d['b'], d['c']) 

    d = {'a' : 0, 'b' : 0, 'c':0 }
    i,j = 0, 0 

    minLength = len(strs) + 1
    while i < len(strs) and strs[i] != 'a':
        i+=1

    j = i
    while j < len(strs):
        d[ strs[j] ] += 1
        curr = j - i + 1
        while i < len(strs) and valid() and curr >= 2:
            minLength = min(minLength, curr)
            d[strs[i]] -= 1
            i += 1

        while i < len(strs) and strs[i] != 'a':
            d[strs[i]] -= 1
            i+=1 
        j = max(j,i) + 1
    while i < len(strs):
        curr = j - i 

        if curr >= 2 and valid():
            minLength = min(minLength, curr)

        d[strs[i]] -= 1
        i += 1
    if minLength == len(strs) + 1:
        return -1
    return minLength

nums = int(input())
ans = []
for i in range(nums):
    input()
    vals = input()
    ans.append(main(vals))
print(*ans, sep='\n')