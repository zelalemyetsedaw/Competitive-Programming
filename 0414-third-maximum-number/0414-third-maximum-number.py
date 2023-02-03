class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        
        firstmax = max(nums)
        nums.remove(firstmax)
        
        if(len(nums)!=0):
            secondmax = max(nums)
            nums.remove(secondmax)
        if(len(nums)!=0):
            thirdmax = max(nums)
        else:
            thirdmax = firstmax
        return thirdmax
        