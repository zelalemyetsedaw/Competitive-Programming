class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        m = len(nums)/2
        d = defaultdict(int)
        
        for i in nums:
            d[i] += 1
            if d[i] > m:
                return i
        