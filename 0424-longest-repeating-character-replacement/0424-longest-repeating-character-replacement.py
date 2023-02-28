class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        array = defaultdict(int)
        maxlength = 0
        for right in range(len(s)):
            array[s[right]] += 1
            
            while right-left+1 - max(array.values()) > k:
                array[s[left]] -= 1
                left += 1
            maxlength = max(maxlength,right-left+1)
            
        return maxlength
                
                
            
        
        