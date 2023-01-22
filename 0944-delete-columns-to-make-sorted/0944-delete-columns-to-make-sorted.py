class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        
        deleted = 0
        for col in range(m):
            for i in range(n-1):
                if strs[i][col]>strs[i+1][col]:
                    deleted += 1
                    break
        return deleted
                    