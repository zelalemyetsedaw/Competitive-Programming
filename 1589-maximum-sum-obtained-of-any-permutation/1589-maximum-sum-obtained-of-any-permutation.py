class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        n = len(nums)
        array = [0]*(n + 1)
        for a, b in requests:
            array[a] += 1
            array[b + 1] -= 1
            
        
        for i in range(1, n):
            array[i] += array[i - 1]
        
        nums.sort()
        array.pop()
        array.sort()
        
        return sum(a*b for a, b in zip(nums, array)) % (10**9 + 7)