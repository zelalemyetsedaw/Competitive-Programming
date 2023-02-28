class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum = [nums[0]]*len(nums)
        
        
        for i in range(1,len(nums)):
            leftsum[i] = leftsum[i-1] + nums[i]
        
            
        total = leftsum[len(nums)-1]
        
        print(leftsum,total)
        for i in range(len(nums)):
            print(total,leftsum[i])
            if i==0 and (total - leftsum[i]) == 0:
                return i
            elif i==0:
                continue
            elif leftsum[i-1] == total - leftsum[i]:
                return i
        return -1
    
    