class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dicts2 = defaultdict(int)
        dicts1 = defaultdict(int)
        
        len1 = len(s1)
        len2 = len(s2)
        
        left = 0
        
        for i in range(len1):
            dicts1[s1[i]] += 1
        
        for right in range(len2):
            dicts2[s2[right]] += 1
            
            if right-left + 1 == len1:
                if dicts1 == dicts2:
                    return True
                dicts2[s2[left]] -= 1
                if dicts2[s2[left]] == 0:
                    dicts2.pop(s2[left])
                left += 1
                
        return False
        