class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # rotate one layer at each time 
        # we calculte the number of layer we use the number of diagonal divided by 2
        n = len(matrix)

        start = 0
        end = n-1
        while start < n // 2:
            for i in range(start, end):
                tmp = matrix[i][start]
                matrix[i][start] = matrix[end][i]
                matrix[end][i] = matrix[n-1-i][end]
                matrix[n-1-i][end] = matrix[start][n-1-i]
                matrix[start][n-1-i] = tmp
            start += 1
            end -= 1
        