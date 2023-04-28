class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[n-1][n-1] or grid[0][0]:
            return -1
        queue = deque([(0,0)])
        visited = set([(0,0)])
        direction = [[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]]
        
        count = 0
        while queue:
            
            l = len(queue)
            count += 1
            r,c = queue.popleft()
            
            if r == n-1 and c ==n-1 :
                    return count
            
            for i in range(l):
                for dx,dy in direction:
                    if min(r+dx,c+dy) >= 0 and max(r+dx,c+dy) != n and (r+dx,c+dy) not in visited and grid[r+dx][c+dy]==0 :
                        queue.append((dx+r,dy+c))
                        visited.add((dx+r,dy+c))
                if i<l-1:
                    r,c = queue.popleft()
                if r == n-1 and c ==n-1 :
                    return count
                    
        return -1
                        
                    
            