class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        d = defaultdict(int)
        left = 0
        maxlen = 0
        answer = 0
        for right in range(len(s)):
            d[s[right]] += 1
            maxlen = max(maxlen,d[s[right]])
            
            if (right - left + 1) - maxlen > k:
                d[s[left]] -= 1
                left += 1
            answer = max(answer,right - left + 1)
                
        return answer