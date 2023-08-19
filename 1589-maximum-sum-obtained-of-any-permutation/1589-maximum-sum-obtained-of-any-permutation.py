class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        temp = [0] * (n + 1)
        for i,j in requests:
            temp[i] += 1
            temp[j+1] -= 1
        for i in range(1,n + 1):
            temp[i] += temp[i-1]
            
        temp.sort(reverse=True)
        nums.sort(reverse=True)
        
        answer = 0
        for i in range(n):
            answer += temp[i] * nums[i]
            
        return answer% (10 ** 9 + 7)
            