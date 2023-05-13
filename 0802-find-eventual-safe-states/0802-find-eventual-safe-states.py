class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        
        out_degree=[0] * n
        
        graphout=[[] for i in range(n)] 
        
        for i in range(n):
            out_degree[i]=len(graph[i])
            for j in graph[i]:
                graphout[j].append(i)
                
        q = deque()
        answer = [] * n
        
        for i in range(n):
            if out_degree[i] == 0:
                q.append(i)
                
        while q:
            u = q.popleft()
            answer.append(u)
            
            for i in graphout[u]:
                
                out_degree[i] -= 1
               
                if out_degree[i] == 0:
                    q.append(i)
                    
        answer.sort()            
        return answer  
        