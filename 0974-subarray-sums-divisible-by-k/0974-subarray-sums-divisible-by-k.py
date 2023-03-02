class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixsum = defaultdict(int)
        psum = 0
        prefixsum[0] = 1
        count = 0
        for i in range(len(nums)):
            psum += nums[i]
            if psum % k in prefixsum:
                count += prefixsum[psum%k]
            
            prefixsum[psum%k] += 1
            
        return count
                