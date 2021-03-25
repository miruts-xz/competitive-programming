class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque()
        visited_left = set()
        visited_right = set()
        visited_left.add(start)
        visited_right.add(start)
        q.append(start)
        while q:
            index = q.popleft()
            if arr[index] == 0:
                return True
            
            i,j = index-arr[index], index+arr[index]
            
            if 0 <= i < len(arr) and i not in visited_left:
                visited_left.add(i)
                q.append(i)
            if 0 <= j < len(arr) and j not in visited_right:
                visited_right.add(j)
                q.append(j)
        return False
