class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def inbound(row,col):
            return 0 <= row <= len(grid)-1 and 0 <= col <= len(grid[0])-1
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        
        def dfs(row,col,count):
            visited[row][col] = True
            
            for rowchange,colchange in directions:
                newrow = row + rowchange
                newcol = col + colchange
                
                if not inbound(newrow,newcol) or grid[newrow][newcol] == 0:
                    count += 1
                
                if inbound(newrow,newcol) and not visited[newrow][newcol] and grid[newrow][newcol] == 1:
                    
                    count = dfs(newrow,newcol,count)
                
                
            return count 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i,j,0)