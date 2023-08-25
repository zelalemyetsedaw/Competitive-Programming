class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        def combinations(ans,index,answer):
            if len(ans) == k:
                answer.append(ans)
                return
            if index > n:
                return 
            
            ans.append(index)
            combinations(ans.copy(),index+1,answer)
            ans.pop()
            combinations(ans.copy(),index+1,answer)
            
        combinations([],1,answer)
        return answer
            
            