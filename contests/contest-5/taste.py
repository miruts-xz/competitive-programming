t = int(input())
from functools import reduce
meals= []
for _ in range(t):
    n, k = map(int, input().split())
    meals.append([n, k]+list(map(int, input().split())))

def get_maximum(meals):
    n, k = meals[0], meals[1]
    maxx = 0
    def dfs(i, subset=[]):
        nonlocal maxx
        if len(subset) == k:
            maxx = max(maxx, reduce(lambda c, x: x|c, subset, 0))
            return
        if i == n+2:
            return
        dfs(i+1, subset+[meals[i]])
        dfs(i+1, subset)
    dfs(2)
    return maxx
print(*[get_maximum(meal) for meal in meals], sep='\n')