class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlength = 0
        end = 0
        window = []
        wlength = 0
        
        while end<len(s):
            window.append(s[end])
            wlength += 1
            while len(window) != len(set(window)):
                window.pop(0)
                wlength -= 1
                
            maxlength = max(maxlength,wlength)
            end += 1
        return maxlength
            
            
        