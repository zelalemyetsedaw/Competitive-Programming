class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftProduct = nums.copy()
        rightProduct = nums.copy()
        
        
        for i in range(1,n):
            leftProduct[i] *= leftProduct[i-1]
        for i in range(n-2,-1,-1):
            rightProduct[i] *= rightProduct[i+1]
            
        for i in range(n):
            if i == 0:
                nums[i] = rightProduct[i+1]
            elif i == n-1:
                nums[i] = leftProduct[i-1]
            else:
                nums[i] = rightProduct[i+1] * leftProduct[i-1]
                
        return nums