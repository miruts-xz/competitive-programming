t = int(input())
ss = []
for i in range(t):
    s = input()
    ss.append(s)
print(*[s.count('w')+s.count('vv') for s in ss], sep=' ')