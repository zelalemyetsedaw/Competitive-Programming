class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        d = defaultdict(int)
        
        for char in words[0]:
            d[char] += 1
        
        for item in words:
            temp = defaultdict(int)
            for i in item:
                temp[i]+=1
            for key in d.keys():
                d[key] = min(d[key],temp[key])
                 
        
        answer = []
        for key in d:
            for j in range(d[key]):
                answer.append(key)
                
        return answer
            
                