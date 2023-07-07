class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        nums = [0]+list(accumulate(nums))
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


            x = y = mid+1
            for i in range(a, mid+1):
                while x<=b and arr[x]-arr[i]<lower:
                    x += 1
                while y<=b and arr[y]-arr[i]<=upper:
                    y += 1
                self.ans += (y-x)


            arr[a:b+1] = lst

        msort(nums, 0, len(nums)-1)
        return self.ans     