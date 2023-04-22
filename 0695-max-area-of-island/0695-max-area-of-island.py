class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        
        def dfs(l,r):
            if l<0 or r<0 or l==len(grid) or r==len(grid[0]) or grid[l][r] == 0 or (l,r) in visited:
                return 0
            
            visited.add((l,r))
            return 1 + dfs(l+1,r) + dfs(l,r+1) + dfs(l-1,r) + dfs(l,r-1)
        
        maxarea = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row,col) not in visited:
                    maxarea = max(maxarea,dfs(row,col))
                    
        return maxarea
                