class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        
        visited = set()
        def  dfs(l,r):
            if l<0 or r<0 or l==len(grid1) or r== len(grid1[0]) or (l,r) in visited or grid2[l][r] == 0:
                return True
            
            res = True
            if grid1[l][r] == 0:
                res = False
            
            visited.add((l,r))
            res = dfs(l+1,r) and res
            res = dfs(l,r+1) and res
            res = dfs(l-1,r) and res
            res = dfs(l,r-1) and res
            
            return res
        
        count = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] and (i,j) not in visited and dfs(i,j):
                    count += 1
                
        return count