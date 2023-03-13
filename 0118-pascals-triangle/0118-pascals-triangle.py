class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ans = []
        def recursion(num):
            if num == 0:
                return [1]
            array = recursion(num-1)
            
            ans.append(array)
            final = [1]
            for i in range(1,len(array)):
                final.append(array[i]+array[i-1])
                
            final.append(1)
            return final
        
        recursion(numRows)
        return ans
            
        