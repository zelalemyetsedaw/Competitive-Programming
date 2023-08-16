class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        visited = defaultdict(int)
        left = 0
        long = 0
        for right in range(len(s)):
            while s[right] in visited:
                visited[s[left]] -= 1
                if visited[s[left]] == 0:
                    visited.pop(s[left])
                left += 1
            visited[s[right]] += 1
            long = max(long,right - left + 1)
            
        return long
                
                
            