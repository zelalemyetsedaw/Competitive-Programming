class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for i in range(32):
            count = 0
            for num in nums:
                if num & (1<<i) == (1<<i):
                    count += 1
            answer |= (count%3) << i
            
        if answer < (1<<31):
            return answer  
        else:
            return answer - (1<<32) 