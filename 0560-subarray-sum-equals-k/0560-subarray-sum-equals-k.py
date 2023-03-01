class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum = defaultdict(int)
        prefixsum[0] = 1
        
        psum = 0
        count = 0
        for i in range(len(nums)):
            psum += nums[i]
            if psum - k in prefixsum:
                count += prefixsum[psum-k]
                
            prefixsum[psum] += 1
            
        return count
                
            