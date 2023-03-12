class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start = 0
        for end in range(len(haystack)):
            s = haystack[start:end+1]
            if len(s) == len(needle):
                if s == needle:
                    return start
                start += 1
                
        return -1