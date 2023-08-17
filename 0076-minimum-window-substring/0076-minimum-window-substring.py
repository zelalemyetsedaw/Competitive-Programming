class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        dict_t = defaultdict(int)
        dict_s = defaultdict(int)
        for item in t:
            dict_t[item] += 1
        
        minlength = len(s) + 1
        leftindex = -1
        rightindex = -1
        left = 0
        have = 0
        for right in range(len(s)):
            if s[right] in dict_t:
                
                dict_s[s[right]] += 1
                if dict_s[s[right]] == dict_t[s[right]]:
                    have += 1
                
            while have == len(dict_t):
                if right-left+1 < minlength:
                    leftindex = left
                    rightindex = right
                    minlength = right-left + 1
                   
                
                if s[left] in dict_s:
                    if dict_t[s[left]] == dict_s[s[left]]:
                        have -= 1
                    dict_s[s[left]] -= 1
                    if dict_s[s[left]] == 0:
                        dict_s.pop(s[left])
                        
                        
                left += 1
                
        if leftindex == -1:
            return ""
        else:
            return s[leftindex:rightindex+1]
                
        
            
        