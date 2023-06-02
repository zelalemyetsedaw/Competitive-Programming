class Solution:
    def nthUglyNumber(self, n: int) -> int:
        arr = [2,3,5]
        def dfs(start) :
            q = deque()
            q.append(start)
            newa = []
            vis = set()
            while q:
                a = q.popleft()
                if len(newa) >= 10000:
                    return newa
                for i in arr:
                    new= i*a
                    if new not in vis:
                        vis.add(new)
                        q.append(new)
                        newa.append(new)
        ans = [1] + dfs(1)
        ans.sort()
        return ans[n-1]        