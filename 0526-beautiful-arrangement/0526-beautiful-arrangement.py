class Solution:
    def countArrangement(self, n: int) -> int:
        def helper(seen,  pointer):
            if len(seen) == n:
                return 1
            
            s = 0
            for i in range(1, n + 1) :
                if i not in seen:
                    if pointer % i == 0 or i % pointer == 0:
                        s += helper(seen | {i}, pointer + 1)
            return s
        
        return helper(set(), 1)