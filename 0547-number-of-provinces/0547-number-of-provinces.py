class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        
        
        n = len(isConnected)
        m = len(isConnected[0])
        parent = {i:i for i in range(1,n+1)}
        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        
        for i in range(n):
            for j in range(m):
                if isConnected[i][j] == 1 and i != j:
                    parent[find(i+1)] = find(j+1)
        answer = set()
        for i in range(1,n+1):
            answer.add(find(i))
            
        return len(answer)
                    
        
        
                
                