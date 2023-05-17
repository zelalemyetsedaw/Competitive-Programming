class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        graph = defaultdict(list)
        
        for item in edges:
            graph[item[0]].append(item[1])
            graph[item[1]].append(item[0])
            
        queue = deque([source])
        visited = set([source])
        
        while queue:
            x = queue.popleft()
            
            for child in graph[x]:
                if child == destination:
                    return True
                if child not in visited:
                    queue.append(child)
                    visited.add(child)
                    
        return False
                
        
            