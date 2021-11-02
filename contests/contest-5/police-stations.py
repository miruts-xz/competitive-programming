from collections import deque, namedtuple
n, k, d = map(int, input().split())
stations = set(map(int, input().split()))

roads = [list(map(int, input().split())) for _ in range(n-1)]
adj_list = [[] for _ in range(n+1)]
Data = namedtuple("Data", ('road', 'city'))
for i, edge in enumerate(roads):
    adj_list[edge[0]].append(Data(i+1, edge[1]))
    adj_list[edge[1]].append(Data(i+1, edge[0]))

def police_stations():
    queue = deque([(0, s) for s in stations])
    visited = set([s for s in stations])
    removed = set()
    final = set()
    while queue:
        dist, city = queue.popleft()
        final.add(city)
        if dist == d: continue
        for road, nbr in adj_list[city]:
            if nbr not in final and (nbr in visited or nbr in stations):
                removed.add(road)
            else:
                visited.add(nbr)
                queue.append((dist+1, nbr))
    print(len(removed))
    print(*removed, sep=' ')
police_stations()
            
            
