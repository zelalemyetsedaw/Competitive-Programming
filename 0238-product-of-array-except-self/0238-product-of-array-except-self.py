class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftproduct = [nums[0]]*n
        rightproduct = [nums[n-1]] *n
        product = [0] * n
        for i in range(1,len(nums)):
            leftproduct[i] = leftproduct[i-1] * nums[i]
            
        for i in range(len(nums)-2,-1,-1):
            rightproduct[i] = rightproduct[i+1] * nums[i]
            
        
        for i in range(len(nums)):
            if i==0:
                product[0] = rightproduct[1]
            elif i==len(nums)-1:
                product[i] = leftproduct[i-1]
            else:
                product[i] = leftproduct[i-1] * rightproduct[i+1]
            
        return product
            