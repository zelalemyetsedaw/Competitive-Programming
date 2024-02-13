class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        if n == 1 and index == 0:
            return maxSum
        minn = 1
        maxx = maxSum
        rightrem = n - index
        leftrem = index
        answer = 0
        while minn < maxx:
            mid = (maxx-minn)//2 + minn
            midd = mid - 1
            rightsum = 0
            leftsum = 0
            totalsum = 0
            if rightrem > mid:
                rightsum = (mid * ( mid + 1)//2) + rightrem - mid
            else:
                rightsum = (mid * (mid + 1))//2 - ((mid-rightrem) * ( mid - rightrem + 1)//2)
            
            if leftrem > midd:
                leftsum = (midd * (midd + 1)//2) + leftrem - midd
            else:
                leftsum = (midd * (midd + 1))//2 - ((midd-leftrem) * (midd - leftrem + 1)//2)
            
            totalsum = rightsum + leftsum
            
            
            if totalsum > maxSum:
                maxx = mid
            else:
                answer = max(answer,mid)
                minn = mid + 1
            

        return answer
