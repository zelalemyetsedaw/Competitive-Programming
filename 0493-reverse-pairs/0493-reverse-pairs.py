class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.ans = 0

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
                if arr[i]<=2*arr[j]:
                    i +=1
                else:
                    self.ans += (mid+1-i)
                    j += 1


            arr[a:b+1] = lst

        msort(nums, 0, len(nums)-1)
        return self.ans