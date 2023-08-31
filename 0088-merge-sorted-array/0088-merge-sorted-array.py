class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        left,right = 0,0
        ans = []
        while left<m and right<n:
            if nums1[left]<nums2[right]:
                ans.append(nums1[left])
                left += 1
            else:
                ans.append(nums2[right])
                right += 1
        while left<m:
            ans.append(nums1[left])
            left += 1
        while right<n:
            ans.append(nums2[right])
            right += 1
        nums1[:]=ans[:]
        