class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        d = defaultdict(list)
        maximum = 0
        for i in range(n):
            x = 1
            y = i
            z = i
            if nums[i] in d:
                x = d[nums[i]][0]
                x += 1
                y = d[nums[i]][1]
                
            if x == 1:
                y = i
            z = i

            d[nums[i]] = [x,y,z]
            maximum = max(maximum,x)
         
        answer = float("inf")
        for key in d:
            if d[key][0] == maximum:
                answer = min(d[key][2]-d[key][1]+1,answer)

        return answer

        



        
