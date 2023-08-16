class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        dict_p = defaultdict(int)
        dict_s = defaultdict(int)
        lengthp = len(p)
        
        for i in p:
            dict_p[i] += 1
        
        left = 0
        answer = []
        for right in range(len(s)):
            dict_s[s[right]] += 1
            if right - left == lengthp - 1:
                if dict_s == dict_p:
                    answer.append(left)
                dict_s[s[left]] -= 1
                if dict_s[s[left]] == 0:
                    dict_s.pop(s[left])
                left += 1
        return answer
                
            
            