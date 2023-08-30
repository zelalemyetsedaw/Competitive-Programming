class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        def dfs(stack):
            while stack:
                child = stack.pop()
                for ch in graph[child]:
                    if ch not in visited:
                        stack.append(ch)
                        visited.add(ch)
        
        n = len(isConnected)
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    
                    
        visited = set()
        stack = []
        count = 0
        
        for i in graph:
            if i not in visited:
                stack.append(i)
                dfs(stack)
                count += 1
        
                        
        return count
                
                