class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left = 0
        row = len(matrix)
        col = len(matrix[0])
        right = (row * col) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid//col][mid % col] > target:
                right = mid-1
            elif matrix[mid//col][mid % col] < target:
                left = mid + 1
            else:
                return True
            
        return False