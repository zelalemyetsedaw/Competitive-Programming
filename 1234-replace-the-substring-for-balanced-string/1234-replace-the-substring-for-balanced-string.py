class Solution:
    def balancedString(self, s: str) -> int:
        dicts = defaultdict(int)
        
        for i in s:
            dicts[i] += 1
            
        n = len(s)/4
        extras = defaultdict(int)
        for i in s:
            if dicts[i] > n:
                extras[i] = dicts[i]-n
        if not extras:
            return 0
        left = 0
        right = 0
        
        
        res = len(s)
        for right in range(len(s)):
            if s[right] in extras:
                extras[s[right]] -= 1
            
            while max(extras.values()) <= 0:
                res = min(res, right-left+1)
                if s[left] in extras:
                    extras[s[left]] += 1
                left += 1
                
        return res
                
            
            