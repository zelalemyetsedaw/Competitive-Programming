class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        self.ans = 0
        nums = [nums1[i]-nums2[i] for i in range(len(nums1))]

        def msort(arr, lo, hi):
            if lo<hi:
                mid = (lo+hi)//2
                msort(arr, lo, mid)
                msort(arr, mid+1, hi)
                merge(arr, lo, mid, hi)

        def merge(arr, a, mid, b):
            i, j = a, mid+1
            lst = []
            while(i<=mid and j<=b):
                if arr[i]<=arr[j]:
                    lst.append(arr[i])
                    i += 1
                else:
                    lst.append(arr[j])
                    j += 1

            lst.extend(arr[i:mid+1])
            lst.extend(arr[j:b+1])


            i, j = a, mid+1
            while(i<= mid and j<=b):
                if arr[i]>arr[j]+diff:
                    j +=1
                else:
                    self.ans += b-j+1
                    i += 1


            arr[a:b+1] = lst

        msort(nums, 0, len(nums)-1)
        return self.ans  