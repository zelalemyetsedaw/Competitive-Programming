class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        freshset = set()
        queue = deque([])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    freshset.add((r,c))
                elif grid[r][c] == 2:
                    queue.append((r,c))
        count = 0            
        while queue and freshset:
            n = len(queue)
            for i in range(n):
                temp = queue.popleft()
                r= temp[0]
                c = temp[1]
                if (r+1,c) in freshset:
                    freshset.remove((r+1,c))
                    queue.append((r+1,c))
                if (r,c+1) in freshset:
                    freshset.remove((r,c+1))
                    queue.append((r,c+1))
                if (r-1,c) in freshset:
                    freshset.remove((r-1,c))
                    queue.append((r-1,c))
                if (r,c-1) in freshset:
                    freshset.remove((r,c-1))
                    queue.append((r,c-1))
            count += 1
        if freshset:
            return -1
        return count
                    