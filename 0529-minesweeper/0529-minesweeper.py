class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        direction = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        m = len(board)
        n = len(board[0])
        sets = set(["1","2","3","4","5","6","7","8"])
        
        def dfs(r,c):
            
            if r<0 or c<0 or r==m or c == n or board[r][c] == "B":
                return
            if board[r][c] == "M":
                board[r][c] = "X"
                return 
            
            flag = False
            count = 0
            for i,j in direction:
                if r+i<0 or c+j<0 or r+i==m or c+j == n:
                    continue
                   
                if board[r+i][c+j] == "M":
                    flag = True
                    count += 1
            if flag == True:
                board[r][c] = str(count)
                return
            else:
                board[r][c] = "B"
                
            for i,j in direction:

                dfs(r+i,c+j)
          
        dfs(click[0],click[1])
        return board