class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        q = []
        for item in queries:
            s = sorted(item)[0]
            q.append(item.count(s))
        w = []
        for item in words:
            s = sorted(item)[0]
            w.append(item.count(s))
        print(q)  
        w.sort()
        
        ans = [0]* len(q)
        for i in range(len(q)):
            l = 0
            r = len(w) - 1
            while (l <= r):
                m = (r + l) // 2
                if (w[m] <= q[i]):
                    l = m + 1
                else:
                    r = m - 1
                
            
            ans[i] = len(w) - l
        
           
            
        return ans
            