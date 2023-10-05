class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        
        nums.sort()
        n = len(nums)
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        
        inlinecount = defaultdict(int)

        counter = 0  
        for i in range(n-1):
            if i == 0:
                inlinecount[nums[i]] += 1
            
            else:
                temp = (i-0-inlinecount[nums[i]]) * (n-1-i-(count[nums[i]]-inlinecount[nums[i]]-1))
                inlinecount[nums[i]] += 1
                counter += temp
                
        return counter
            