class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def inbound(r,c):
            return 0 <= r <=len(grid)-1 and 0 <= c <= len(grid[0]) - 1
        
        visited = set()
        def dfs(r,c):
            if not inbound(r,c) or grid[r][c] == "0" or (r,c) in visited:
                return 
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
        count = 0   
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    count += 1
                   
        return count