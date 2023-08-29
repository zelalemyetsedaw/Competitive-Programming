class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def inbound(r,c):
            return 0 <= r < m and 0 <= c < n
        
        
        visited = set()
        queue = deque()
        ones = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    visited.add((i,j))
                elif grid[i][j] == 1:
                    ones += 1
        
        second = 0
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        while queue:
            level = len(queue)
            second += 1
            
            for i in range(level):
                dx,dy = queue.popleft()
                
                for a,b in directions:
                    newdx,newdy = dx+a,dy+b
                    if inbound(newdx,newdy) and (newdx,newdy) not in visited and grid[newdx][newdy] == 1:
                        queue.append((newdx,newdy))
                        visited.add((newdx,newdy))
                        grid[newdx][newdy] = 2
                        ones -= 1
                        
        if ones > 0:
            return -1
        return second - 1 if second > 0 else 0
                    
                