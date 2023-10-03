class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        n = len(s)
        dif = []
        for i in range(n):
            dif.append(abs(ord(s[i]) - ord(t[i])))
            
        left = 0
        maxx = 0
        windowsumm = 0
        for right in range(n):
            windowsumm += dif[right]
            while windowsumm > maxCost:
                windowsumm -= dif[left]
                left += 1
            maxx = max(right-left+1,maxx)
            
        return maxx
            