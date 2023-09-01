class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        m = len(nums1)
        n = len(nums2)
        
        i = 0
        j = 0
        merged = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        while i < m:
            merged.append(nums1[i])
            i += 1
        while j < n:
            merged.append(nums2[j])
            j += 1
            
        if (m + n) % 2 == 0:
            return (merged[(m+n)//2]  + merged[(m+n)//2 - 1])/2
        else:
            return merged[(m+n)//2]
                