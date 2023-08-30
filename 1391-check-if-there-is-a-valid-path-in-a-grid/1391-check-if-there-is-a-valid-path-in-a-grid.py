class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        m = len(grid)
        n = len(grid[0])
        
        def inbound(r,c):
            return 0 <= r < m and 0 <= c < n
        
        directions = {
            1:[(0,-1),(0,1)],
            2:[(1,0),(-1,0)],
            3:[(0,-1),(1,0)],
            4:[(0,1),(1,0)],
            5:[(-1,0),(0,-1)],
            6:[(-1,0),(0,1)]
        }
        
        stack = [(0,0)]
        destination = (m-1,n-1)
        visited = set([(0,0)])
        flag = False
        while stack:
            r,c = stack.pop()
            if (r,c) == destination:
                flag = True
            
            
            for dr,dc in directions[grid[r][c]]:
                newrow , newcol = r + dr, c + dc
                
                
                if inbound(newrow,newcol) and (newrow,newcol) not in visited and (-dr,-dc) in directions[grid[newrow][newcol]]:
                    stack.append((newrow,newcol))
                    visited.add((newrow,newcol))
                    
                    
        return flag
                        
                
