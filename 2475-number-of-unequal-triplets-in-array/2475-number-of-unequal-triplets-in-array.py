class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if j > i and k > j:
                        
                        if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                            
                            count += 1
                            
        return count
            