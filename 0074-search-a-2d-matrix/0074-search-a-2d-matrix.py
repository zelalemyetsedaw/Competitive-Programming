class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        for i in range(n):
            if target in matrix[i]:
                return True
        return False