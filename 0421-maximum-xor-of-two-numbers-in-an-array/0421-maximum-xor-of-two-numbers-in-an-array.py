class Solution:
    def findMaximumXOR(self, lists: List[int]) -> int:
        
        
        
        answer = 0
        mask = 0
        for i in range(31, -1, -1):
            mask |= 1<<i
            found = set([item & mask for item in lists])

            initial = answer | 1<<i
            for i in found:
                if initial^i in found:
                    answer = initial
                    break

        return answer
