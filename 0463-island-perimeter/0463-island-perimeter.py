class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def inbound(row,col):
            return 0 <= row <= len(grid)-1 and 0 <= col <= len(grid[0])-1
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        
        
        def dfs(row,col):
            if not inbound(row,col) or grid[row][col] == 0  :
                return 1
            if visited[row][col]:
                return 0
            visited[row][col] = True
            count = 0
            
            for rowchange,colchange in directions:
                newrow = row + rowchange
                newcol = col + colchange
                count += dfs(newrow,newcol)
                
                
            return count 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i,j)
                 