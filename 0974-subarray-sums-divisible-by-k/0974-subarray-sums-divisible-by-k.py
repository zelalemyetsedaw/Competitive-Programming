class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        
        count = 0
        total = 0
        
        for i in range(len(nums)):
            total += nums[i]
            if total % k in d:
                count += d[total % k]
                
            d[total%k] += 1
            
        return count 