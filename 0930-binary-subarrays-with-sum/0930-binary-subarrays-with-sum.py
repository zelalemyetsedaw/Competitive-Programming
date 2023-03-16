class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        dicts = defaultdict(int)
        count = 0
        psum = 0
        dicts[0] = 1
        for i in nums:
            psum += i
            if psum - goal in dicts:
                count += dicts[psum-goal]
            
            dicts[psum] += 1
            
        return count