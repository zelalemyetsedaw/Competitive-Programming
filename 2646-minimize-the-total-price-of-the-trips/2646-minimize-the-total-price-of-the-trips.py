class Solution:
    def __init__(self):
        self.dp = []
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        
        g = [[] for _ in range(n)]
        self.dp = [[-1, -1] for _ in range(n)]
        
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        
        contri = [0] * n
        for t in trips:
            curr = []
            self.makeContri(t[0], curr, contri, t[1], g, -1)
        
        return self.dfs(contri, price, 0, g, -1, False)
        
        

    
    def makeContri(self, node, curr, contri, end, g, p):
        curr.append(node)
        
        if end == node:
            for i in curr:
                contri[i] += 1
            curr.pop()
            return
        
        for ch in g[node]:
            if ch != p:
                self.makeContri(ch, curr, contri, end, g, node)
        
        curr.pop()
    
    def dfs(self, contri, pr, node, g, p, parentHalved):
        res1 = (contri[node] * pr[node]) // 2
        res2 = contri[node] * pr[node]
        
        if self.dp[node][parentHalved] != -1:
            return self.dp[node][parentHalved]
        
        for ch in g[node]:
            if ch != p:
                res2 += self.dfs(contri, pr, ch, g, node, False)
        
        if parentHalved:
            self.dp[node][parentHalved] = res2
            return res2
        
        for ch in g[node]:
            if ch != p:
                res1 += self.dfs(contri, pr, ch, g, node, True)
        
        self.dp[node][parentHalved] = min(res1, res2)
        return self.dp[node][parentHalved]
    
    


        