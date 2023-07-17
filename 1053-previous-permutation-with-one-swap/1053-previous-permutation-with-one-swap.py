class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        
        first = arr[0]
        firstindex = 0
        lastindex = 1
        
        flag = False
        
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                firstindex = i
                lastindex = i+1
                flag = True
            elif arr[i+1] < arr[firstindex] and arr[i+1] != arr[lastindex]:
                lastindex = i+1
        if not flag:
            return arr
        else:
            temp = arr[firstindex]
            arr[firstindex] = arr[lastindex]
            arr[lastindex] = temp
            
        return arr