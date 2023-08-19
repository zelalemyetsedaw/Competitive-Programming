class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
         
        dicts = defaultdict(int)
        dicts[0] = 1
        count = 0
        for i in range(len(nums)):
            if nums[i] - k in dicts:
                count += dicts[nums[i]-k]
            dicts[nums[i]] += 1
            
        return count
            