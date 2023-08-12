class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        maxNumber = arr[0]
        
        i = 0
        j = len(arr)-1
        answer = []
        while j > 0:
            maxx = 0
            
            for k in range(j+1):
                if arr[k] > arr[maxx]:
                    maxx = k
            
            # if maxx != j:
            arr[:maxx+1] = reversed(arr[:maxx+1])
            answer.append(maxx+1)
            arr[:j+1] = reversed(arr[:j+1])
            answer.append(j+1)
            j -= 1
            
        return answer
                    
                
            