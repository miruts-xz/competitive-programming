# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    r = []
    f_dict = {}
    for s in strings:
        f_dict[s] = f_dict.get(s, 0) + 1
    for q in queries:
        r.append(f_dict.get(q, 0))
    return r


print(matchingStrings(['ab', 'ab', 'abc', 'da'], ['ab', 'abc', 'nw']))
