class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def rec(nums, pair):
            if len(pair) == len(nums):
                ans.add(pair)
                return
            for num in nums:
                if num not in pair:
                    rec(nums, pair + (num,))

        ans = set()
        rec(nums, ())
        return ans