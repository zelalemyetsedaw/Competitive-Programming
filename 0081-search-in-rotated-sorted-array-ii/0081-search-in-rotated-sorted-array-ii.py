class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = left + (right-left)//2
            
            if nums[left] == nums[right] and left != right:
                right -= 1
            else:
                if (nums[mid] >= nums[0] and target >= nums[0]) or (nums[mid] < nums[0] and target < nums[0]) :
                    midelement = nums[mid]
                else:
                    if target < nums[0]:
                        midelement = -float("inf")
                    else:
                        midelement = float("inf")
            
                #normal binary search
                if target == midelement:
                    return True
                elif target > midelement:
                    left = mid + 1
                else:
                    right = mid - 1
                
        return False