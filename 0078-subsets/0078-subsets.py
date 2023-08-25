class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def subsets(temp,ans,index):
            if temp not in ans:
                ans.append(temp[:])
            if index >= len(nums):
                return
            
            temp.append(nums[index])
            subsets(temp,ans,index+1)
            temp.pop()
            subsets(temp,ans,index+1)
            
        subsets([],ans,0)
        return ans
            