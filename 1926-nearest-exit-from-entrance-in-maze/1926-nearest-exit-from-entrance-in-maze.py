class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row = len(maze)
        col = len(maze[0])
        
        queue = deque([entrance])
        visited = set()
        visited.add((entrance[0],entrance[1]))
        
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        count = 0
        while queue:
            l = len(queue)
            count += 1
            
            for i in range(l):
                r,c = queue.popleft()
                
                for dx,dy in direction:
                    r1,c1 = r+dx,c+dy
                    
                    if r1>=0 and r1<=row-1 and c1>=0 and c1 <= col-1 and maze[r1][c1] == "." and (r1,c1) not in visited:
                        queue.append((r1,c1))
                        visited.add((r1,c1))
                        
                    elif (r1==-1 or c1==-1 or r1==row or c1 == col) and count > 1:
                        return count-1
                    
        return -1
                        
                