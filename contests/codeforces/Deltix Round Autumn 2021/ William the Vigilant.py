
def solve(n, q, chars, queries):
    ans = []
    count = chars.count('abc')
    char_array = [c for c in chars]
    for ind, char in queries:
        ind = int(ind)
        # left = 
        temp = char_array[ind-2:ind+3]
        ts = ''.join(temp)
        prev = temp.count('abc')
        temp[2] = char
        cur = ''.join(temp).count('abc')
        count = count - prev + cur
        ans.append(count)
if __name__ == '__main__':
    n, q = map(int, input().split())
    chars = input()
    queries = []
    for _ in range(q):
        queries.append(input().split())
    ans = solve(n, q, chars, queries)
    print(*ans, sep='\n')