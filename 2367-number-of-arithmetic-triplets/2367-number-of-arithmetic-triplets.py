class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        sets = set(nums)
        count = 0
        for item in nums:
            if item - diff in sets and item + diff in sets:
                count += 1
                
        return count