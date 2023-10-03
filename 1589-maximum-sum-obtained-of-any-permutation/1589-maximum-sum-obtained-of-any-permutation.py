class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        n = len(nums)
        prefixsum = [0] * (n + 1)
        for i,j in requests:
            prefixsum[i] += 1
            prefixsum[j+1] -= 1
            
        for i in range(1,n+1):
            prefixsum[i] += prefixsum[i-1]
            
        prefixsum.sort(reverse=True)
        nums.sort(reverse = True)
        answer = 0
        for i in range(n):
            answer += (prefixsum[i] * nums[i])
            
        return answer%(10**9 + 7)
            
            