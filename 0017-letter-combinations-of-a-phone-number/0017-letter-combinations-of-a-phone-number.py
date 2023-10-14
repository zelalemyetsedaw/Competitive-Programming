class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        d = defaultdict(list)
        
        k = 0
        for i in range(2,10):
            for j in range(3):
                d[str(i)].append(chr(97+k))
                k+=1
            if i == 7 or i==9:
                d[str(i)].append(chr(97+k))
                k+=1
                
        n = len(digits)
        if n == 0:
            return []
        answer = []
        def backtrack(index,temp):
            nonlocal answer
            if index == n:
                answer.append(temp)
                return 
            
            for i in d[digits[index]]:
                
                backtrack(index+1,temp+i)
                
        backtrack(0,"")
        return answer
                