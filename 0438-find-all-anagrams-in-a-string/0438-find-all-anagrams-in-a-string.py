class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        dicts = defaultdict(int)
        dictp = defaultdict(int)
        for i in range(len(p)):
            dictp[p[i]] += 1
        
        end = 0
        start = 0
        result = []
        while end<len(s):
            dicts[s[end]] += 1
            if end-start + 1 == len(p):
                if dicts == dictp:
                    result.append(start)
                dicts[s[start]] -= 1
                if(dicts[s[start]]==0):
                    dicts.pop(s[start])
                start += 1
            end += 1
            
        return result           
        