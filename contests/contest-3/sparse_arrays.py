# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    r = []
    for q in queries:
        r.append(strings.count(q))
    return r
