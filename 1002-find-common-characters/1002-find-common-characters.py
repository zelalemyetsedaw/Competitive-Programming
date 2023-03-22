class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        ans = [i for i in words[0]]
        for item in words:
            temp = []
            for j in item:
                if j  in ans:
                    temp.append(j)
                    ans.remove(j)
                    
            ans = temp
                    
        return ans
    
    
            