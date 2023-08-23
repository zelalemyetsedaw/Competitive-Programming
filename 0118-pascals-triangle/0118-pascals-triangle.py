class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        # def pascal(n):
        #     if n == 1:
        #         return [[1]]
        #     array = pascal(n-1)
        #     array2 = [0] + array[-1] + [0]
        #     row = []
        #     for i in range(len(array2) - 1):
        #         row.append(array2[i] + array2[i+1])
        #     array.append(row)
        #     return array
        # return pascal(numRows)
                
        answer = [[1]]
        
        for i in range(numRows-1):
            temp = [0] + answer[-1] + [0]
            
            for j in range(len(temp) - 1):
                temp[j] = temp[j]+temp[j+1]
            temp.pop()
            answer.append(temp)
            
        return answer

