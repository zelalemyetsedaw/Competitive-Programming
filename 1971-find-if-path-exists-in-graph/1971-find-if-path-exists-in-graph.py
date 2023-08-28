class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        visited = set([source])
        stack = [source]
        
        while stack:
            source = stack.pop()
            if source == destination:
                return True
            
            for child in graph[source]:
                if child not in visited:
                    visited.add(child)
                    stack.append(child)
                    
        return False
        