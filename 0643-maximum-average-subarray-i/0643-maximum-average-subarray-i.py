class Solution(object):
    def findMaxAverage(self, nums, k):
        start = 0
        end = k
        wsum = 0.0
        
        for i in range(k):
            wsum += nums[i]
        maxavg = wsum/k
        while end<len(nums):
            wsum = wsum + nums[end] - nums[start]
            maxavg = max(wsum/k,maxavg)
            start += 1
            end += 1
            
        return maxavg