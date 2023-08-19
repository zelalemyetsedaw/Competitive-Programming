class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
                
        d = defaultdict(int)
        count = 0
        total = 0
        d[0] = 1
        for i in range(len(nums)):
            total += nums[i]
            if total - k in d:
                count += d[total-k]
            d[total] += 1
            
        return count
        
                