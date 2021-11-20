
def solve(n,m,messages):
    imps = set()
    crews = set()
    for sayer, sayee, type in messages:
        # it's a truth
        if sayer in crews:
            if type == 'i' and sayee not in crews:
                imps.add(sayee)
            elif type == 'c' and sayee not in imps:
                crews.add(sayee)
            else:
                return -1
        # it's a lie
        elif sayer in imps:
            if type == 'c' and sayee not in crews:
                imps.add(sayee)
            elif type == 'i' and sayee not in imps:
                crews.add(sayee)
            else:
                return -1
        elif type == 'i':
            if sayee in imps:
                crews.add(sayer)
            elif sayee in crews:
                imps.add(sayee)
            else:
                crews.add(sayer)
                imps.add(sayee)
        else:
            if sayee in crews:
                imps.add(sayer)
            elif sayee in imps:
                imps.add(sayer)
            else:
                imps.add(sayee)
                imps.add(sayer)
    return n-len(crews)

if __name__ == '__main__':
    ans = []
    for _ in range(int(input())):
        n, m = map(int, input().split())
        messages = [
            input().split() for _ in range(m)
        ]
        messages = [[int(p1), int(p2), c[0]] for p1, p2, c in messages]
        ans.append(solve(n,m,messages))
    print(*ans, sep='\n')