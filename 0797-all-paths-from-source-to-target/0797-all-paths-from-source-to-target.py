class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        g = defaultdict(list)
        for i in range(len(graph)):
            g[i] = graph[i]
        n = len(graph)    
        
        
        answer = []
        
        def dfs(node,cur):
            if node == n-1:
                cur.append(node)
                answer.append(cur.copy())
                return
                
            
            cur.append(node)
            for child in g[node]:
                dfs(child,cur)
                cur.pop()
                    
        dfs(0,[])
        
        return answer
                