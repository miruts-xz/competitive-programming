class Solution(object):
    def isBipartite(self, graph):

        visited = [False] * len(graph)
        color = [-1] * len(graph)
        color[0] = 0

        for j in range(len(graph)):
            if visited[j] == False:
                visited[j] = True
                q = [j]
                val = self.checkisBipartite(graph, visited, q, color)
                if val == False:
                    return val
        return True

    def checkisBipartite(self, graph, visited, q, color):
        while len(q) > 0:
            top = q.pop(0)
            for i in graph[top]:
                if visited[i] == True:
                    a = color[i]
                    if color[top] == a:
                        return False
                else:
                    color[i] = color[top] ^ 1
                    q.append(i)
                    visited[i] = True
        return True
