
def solve(n, string):
    string = [c for c in string]
    ans = 0
    def valid(i, char):
        if char == 'a': return False
        nbr = chr(ord(char)-1)
        return (i-1 >= 0 and string[i-1]==nbr) or (i+1 < len(string) and string[i+1] == nbr)
    _maxxIdx = None
    while string:
        _maxxIdx = None
        for i, c in enumerate(string):
            if valid(i,c):
                if _maxxIdx is not None:
                    if c > string[_maxxIdx]:
                        _maxxIdx = i
                else:
                    _maxxIdx = i
        if _maxxIdx is None: break
        string.pop(_maxxIdx)    
    return n-len(string)



if __name__ == '__main__':
    print(solve(int(input()), input()))