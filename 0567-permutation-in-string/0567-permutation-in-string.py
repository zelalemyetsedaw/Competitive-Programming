class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        dict_s1 = defaultdict(int)
        length1 = len(s1)
        dict_s2 = defaultdict(int)
        
        for i in s1:
            dict_s1[i] += 1
        left = 0   
        for right in range(len(s2)):
            dict_s2[s2[right]] += 1
            if right - left + 1 == length1:
                if dict_s1 == dict_s2:
                    return True
                dict_s2[s2[left]] -= 1
                if dict_s2[s2[left]] == 0:
                    dict_s2.pop(s2[left])
                left += 1
                
        return False
            
        