class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        nums  = set([i+1 for i in range(1000)])

        for n in arr:
            nums.remove(n)
        ans = list(nums)
        ans.sort()
        if k > len(ans) - 1:
            return 1000 + k - len(ans)
        return ans[k-1]