class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        output = []
        for element in nums:
            output.append(nums[element])
            
        return output
            