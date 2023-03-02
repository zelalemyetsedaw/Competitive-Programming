class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
                
        prefixsum = defaultdict(int)
        psum = 0
        prefixsum[0] = 1
        count = 0
        for i in range(len(nums)):
            psum += nums[i]
            if psum - k in prefixsum:
                count += prefixsum[psum-k]
            
            prefixsum[psum] += 1
            
        return count
                
            