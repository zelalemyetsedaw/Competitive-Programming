class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowcounter = defaultdict(set)
        colcounter = defaultdict(set)
        subboxes = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rowcounter[r] or board[r][c] in colcounter[c] or board[r][c] in subboxes[(r//3,c//3)]:
                    return False
                rowcounter[r].add(board[r][c])
                colcounter[c].add(board[r][c])
                subboxes[(r//3,c//3)].add(board[r][c])
                
        return True