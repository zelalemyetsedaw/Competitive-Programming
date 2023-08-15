class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        lastindex = defaultdict(int)
        for i in range(len(s)):
            lastindex[s[i]] = i
            
        initialindex = 0
        left = 0
        right = 0
        ans = []
        while left < len(s):
            
            if lastindex[s[left]] > right:
                right = lastindex[s[left]]
                
            if left == right:
                ans.append(right - initialindex + 1)
                initialindex = left + 1
            left += 1
        
        return ans
                
                
            
            
            
