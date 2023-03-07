class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        array = [(p,i) for i,p in enumerate(temperatures)]
        
        stack = []  # monotonic decreasing order stack
        result = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            while stack and array[i][0] > stack[-1][0]:
                    result[stack[-1][1]] = i-stack[-1][1]
                    stack.pop()
            stack.append(array[i])
            
                
        return result
                
            