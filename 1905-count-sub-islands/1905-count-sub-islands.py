class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        m = len(grid1)
        n = len(grid1[0])
        
        def inbound(r,c):
            return 0 <= r < m and 0 <= c < n
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set()
        def dfs(i,j):
            stack = []
            stack.append((i,j))
            visited.add((i,j))
            countgrid1 , countgrid2 = 0,0
            while stack:
                r,c = stack.pop()
                if grid1[r][c] == 1:
                        countgrid1 += 1
                countgrid2 += 1


                for dr,dc in directions:
                    newrow,newcol = r + dr,c + dc
                    if inbound(newrow,newcol) and grid2[newrow][newcol] != 0 and (newrow,newcol) not in visited:
                        stack.append((newrow,newcol))
                        visited.add((newrow,newcol))
            return countgrid2 == countgrid1
        
        answer = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and (i,j) not in visited and dfs(i,j):
                    answer += 1
        
        return answer
        
                
                
            
        
        