
def solve(n1, p1, n2, p2):
    if len(str(n1))+p1 > len(str(n2))+p2:
        return '>'
    elif len(str(n1))+p1 < len(str(n2))+p2:
        return '<'
    if p1 > p2:
        p1 -= p2
        p2 = 0
    else:
        p2 -= p1
        p1 = 0
    num1 = int(str(n1)+'0'*p1)
    num2 = int(str(n2)+'0'*p2)
    if num1 > num2:
        return '>'
    elif num2 > num1:
        return '<'
    return '='

if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        n1, p1 = map(int, input().split())
        n2, p2 = map(int, input().split())
        ans.append(solve(n1, p1, n2, p2))
    print(*ans, sep='\n')