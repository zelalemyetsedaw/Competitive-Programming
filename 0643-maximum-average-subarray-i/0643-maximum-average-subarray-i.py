class Solution(object):
    def findMaxAverage(self, nums, k):
       
        
        start,end = 0,0
        maxsum = -float("inf")
        cursum = 0.0
        curavg = 0
        while(end<len(nums)):
            cursum += nums[end]
            if(end-start+1==k):
                curavg = cursum / k
                maxsum = max(maxsum,curavg)
                cursum -= nums[start]
                start += 1
            
            end += 1
                
        return maxsum
                
        