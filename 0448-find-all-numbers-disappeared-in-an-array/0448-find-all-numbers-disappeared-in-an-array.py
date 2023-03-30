class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            temp = nums[i]
            if temp != nums[temp-1] and i != temp - 1:
                nums[i],nums[temp-1] = nums[temp-1],temp
                
            else:
                i += 1
        answer = []       
        for i in range(len(nums)):
            if i+1 != nums[i]:
                answer.append(i+1)
                
        return answer
                