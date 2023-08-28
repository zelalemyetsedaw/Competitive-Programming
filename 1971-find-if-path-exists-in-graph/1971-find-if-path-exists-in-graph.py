class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        visited = set()
        flag = False
        def dfs(source,destination,flag):
            if source == destination:
                flag = True
            visited.add(source)
            
            for child in graph[source]:
                if child not in visited:
                    flag = dfs(child,destination,flag)
            return flag
            
            
            
        
        return dfs(source,destination,flag)