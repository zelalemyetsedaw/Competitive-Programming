class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        
        first = arr[0]
        firstindex = 0
        last = arr[1]
        lastindex = 0
        
        if sorted(arr) == arr:
            return arr
        
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                first = arr[i]
                firstindex = i
                last = arr[i+1]
                lastindex = i+1
            elif arr[i+1] < first and arr[i+1] !=last:
                last = arr[i+1]
                lastindex = i+1
        if firstindex == len(arr)-1:
            return arr
        else:
            arr[firstindex] = last
            arr[lastindex] = first
            
        return arr