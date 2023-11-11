class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        prefix = [0] * 102

        for item in logs:
            prefix[item[0]-1950] += 1
            prefix[item[1]-1950] -= 1

        for i in range(1,102):
            prefix[i] += prefix[i-1]
        
        maxi = max(prefix)
        for i in range(102):
            if prefix[i] == maxi:
                return i+1950