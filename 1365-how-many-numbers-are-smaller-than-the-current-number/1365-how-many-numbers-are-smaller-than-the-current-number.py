class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counts = [0 for x in range(101)]
        answer = [0 for x in range(len(nums))]
        for i in range(len(nums)):
            counts[nums[i]] += 1
        for i in range(1,101):
            counts[i] += counts[i-1]
        for i in range(len(nums)):
            if(nums[i]!=0):
                answer[i] = counts[nums[i]-1]
            else:
                answer[i] = 0
        return answer