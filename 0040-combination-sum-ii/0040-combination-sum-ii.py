class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort()
        def combinationsum(index, cur, target):
            if target == 0:
                answer.append(cur.copy())
                return
            elif target < 0:
                return
            
            prev = -1
            for i in range(index,len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                combinationsum(i+1,cur,target - candidates[i])
                cur.pop()
                prev = candidates[i]
            
        combinationsum(0,[],target)
        return answer
            
            
        
        summ = 0
        cur = []
        index = 0
        combinationsum(index,cur,summ)
        return answer
                