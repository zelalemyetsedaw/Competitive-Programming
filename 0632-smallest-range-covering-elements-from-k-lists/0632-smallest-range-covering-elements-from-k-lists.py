class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        array = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                array.append((nums[i][j],i))
        
        array.sort()
        
        ans = [0,array[-1][0]+1]
        k = len(nums)
        
        window =[0]*k
        required = 0
        left = 0
        
        
        for right in range(len(array)):
            
            newn,idx = array[right]
            if window[idx] == 0:
                required += 1
            window[idx] += 1
            
            while required == k:
                if array[right][0]-array[left][0] < ans[1] - ans[0]:
                    ans = [array[left][0],array[right][0]]
                item,num = array[left]
                window[num] -= 1
                if window[num] == 0:
                    required -= 1
                left += 1
                
        return ans
    
                
            
                
            
            
        
        
                