class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
         
        dicts = defaultdict(int)
        dicts[0] = 1
        count = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            if total - k in dicts:
                count += dicts[total-k]
            dicts[total] += 1
            
        return count
            