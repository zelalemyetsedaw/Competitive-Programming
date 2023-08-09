class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        arr = [0] * 1001
        
        for item in arr1:
            arr[item] += 1
         
        answer = [0] * len(arr1)
        i = 0
        for item in arr2:
            while arr[item] > 0:
                answer[i] = item
                arr[item] -= 1
                i += 1
                
        for j in range(1001):
            while arr[j] > 0:
                answer[i] = j
                arr[j] -= 1 
                i += 1
        return answer
                
            
            