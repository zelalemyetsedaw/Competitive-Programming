class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n, visited = len(grid), set()

        def dfs(i,j):
            if i < 0 or j < 0 or i >= n or j >= n or (i,j) in visited or grid[i][j] == 0:
                return 

            visited.add((i,j))

            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)

        def bfs():
            stack = []

            for i,j in visited:
                stack.append((i,j,0))

            while stack:
                x, y, total = stack.pop(0)

                for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                    if 0 <= nx < n and 0 <= ny < n and (nx,ny) not in visited:
                        if grid[nx][ny] == 1:
                            return total
                        visited.add((nx,ny))
                        stack.append((nx,ny,total+1))
                        

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i,j)
                    return bfs()        