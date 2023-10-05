class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        n = len(nums)
        maxanswer = 0
        
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if j > i and k > j:
                        temp = (nums[i]-nums[j]) * nums[k]
                        maxanswer = max(temp,maxanswer)
        return maxanswer
                            
                            
                        
                        
                    