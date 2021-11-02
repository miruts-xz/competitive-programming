a, b, c, d = map(int, input().split())
tries = (2/(a/b))-1
b_prob = (tries//2)/(tries)
print(1-b_prob)