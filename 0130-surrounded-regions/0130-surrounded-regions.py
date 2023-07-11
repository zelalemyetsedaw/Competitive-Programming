class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board),len(board[0])
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        array = []
        
        def dfs(r,c):
            if r<0 or c<0 or r==m or c==n or board[r][c] != 'O': return
            board[r][c] = 'z'
            for item in direction:
                dfs(r+item[0],c + item[1])
                
        for i in range(n):
            if board[0][i] == 'O':
                dfs(0,i)
            if board[m-1][i] == 'O':
                dfs(m-1,i)
                
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i,0)
            if board[i][n-1] == 'O':
                dfs(i,n-1)
       
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'z':
                    board[i][j] = 'O'
                    
        return board
                
            