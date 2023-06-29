class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        x = 1
        for item in nums:
            if item > 0 and item > x :
                return x
            if item == x:
                x += 1
        return x