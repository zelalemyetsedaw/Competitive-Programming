class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        visited = set([0])
        
        for i,j in enumerate(rooms):
            graph[i] = j
        
        n = len(rooms)
        queue = deque([0])
        count = 1
        while queue:
            x = queue.popleft()
            for i in graph[x]:
                if i not in visited:
                    count += 1
                    queue.append(i)
                    visited.add(i)
            if count == n:
                return True
        return False
                
            
        