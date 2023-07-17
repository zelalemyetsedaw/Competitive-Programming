class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        if len(nums)<3:
            return False
        
        left = float("inf")
        middle = float("inf")
        
        for item in nums:
            if item > middle:
                return True
            elif item > left and item < middle:
                middle = item
            elif item < left:
                left = item
                
        return False