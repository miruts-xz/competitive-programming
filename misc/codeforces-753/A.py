t = int(input())
tests = []
for _ in range(t):
    chars = list([c for c in input()])
    word = input()
    tests.append([word, chars])

def time_taken(alphabets)->int:
    positions = {c: i for i, c in enumerate(alphabets[1])}
    word = alphabets[0]
    ans = 0
    for i in range(1, len(word)):
        ans += abs(positions[word[i]]-positions[word[i-1]])
    return ans
for t in tests:
    print(time_taken(t))