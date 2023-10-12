class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        d = defaultdict(list)
        n = len(strs)
        for i in range(n):
            s = "".join(sorted(strs[i]))
            
            d[s].append(strs[i])
         
        answer = []
        for key in d:
            answer.append(d[key])
            
        return answer
                
        
            