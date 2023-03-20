class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        
        def combinationsum(index, cur, summ):
            if summ == target:
                answer.append(cur.copy())
                return
            elif index >= len(candidates) or summ > target:
                return
            
            cur.append(candidates[index])
            
            combinationsum(index,cur,summ+candidates[index])
            
            cur.pop()
            combinationsum(index+1,cur,summ)
            
            
        
        summ = 0
        cur = []
        index = 0
        combinationsum(index,cur,summ)
        return answer
                