class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        difference = [0] * len(s)
        for i in range(len(s)):
            difference[i] = abs(ord(s[i]) - ord(t[i]))
        
        maxlen = 0
        window = 0
        left = 0
        for right in range(len(s)):
            window += difference[right]
            while window > maxCost:
                window -= difference[left]
                left += 1
                
            maxlen = max(maxlen,right - left + 1)
            
        return maxlen
            