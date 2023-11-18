class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        decstack = []
        minimum = nums[0]

        for num in nums:
            while decstack and decstack[-1][0] <= num:
                decstack.pop()

            if decstack and num > decstack[-1][1]:
                return True

            decstack.append([num,minimum])
            minimum = min(minimum,num)

        return False