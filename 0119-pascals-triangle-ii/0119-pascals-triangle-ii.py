class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        temp = [1]
        for i in range(rowIndex):
            temp = [0] + temp + [0]
            for j in range(len(temp)-1):
                temp[j] += temp[j+1]
            temp.pop()
        return temp
            
#         def pascal(n):
#             if n == 0:
#                 return [1]
            
#             array = [0] + pascal(n-1) + [0]
#             for i in range(len(array) - 1):
#                 array[i] += array[i+1]
#             array.pop()
#             return array
        
#         return pascal(rowIndex)