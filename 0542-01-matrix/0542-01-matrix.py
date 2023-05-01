class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        queue = deque()
        visited = set()
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))
        
        direction = [[0,1],[1,0],[-1,0],[0,-1]]
        while queue:
            l = len(queue)
            
            for i in range(l):
                r,c = queue.popleft()
                for dx,dy in direction:
                    if r+dx >= 0 and r+dx <=  row-1 and c+dy <= col-1 and c+dy >= 0 and (r+dx,c+dy) not in visited:
                        mat[r+dx][c+dy] = mat[r][c]+1
                        queue.append((r+dx,c+dy))
                        visited.add((r+dx,c+dy))
                        
        return mat
                