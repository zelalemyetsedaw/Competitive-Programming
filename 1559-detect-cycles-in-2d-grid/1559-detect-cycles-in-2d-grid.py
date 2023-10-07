class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m,n = len(grid),len(grid[0])
        def inbound(r,c):
            return 0 <= r <= m-1 and 0 <= c <= n-1
        visited = set()
        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(r,c,parent):
            
            startchar = grid[r][c]
            visited.add((r,c))
            
            for x,y in direction:
                newx,newy = r + x , y + c
                if inbound(newx,newy) and grid[newx][newy] == startchar and (newx,newy) != parent:
                    
                    if (newx,newy) in visited:
                        return True
                    if dfs(newx,newy,(r,c)):
                        return True
                
            return False
            
            
            
            
            
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited:
                    if dfs(i,j,(-1,-1)):
                        return True
                    
        return False
            
            
            
        
            