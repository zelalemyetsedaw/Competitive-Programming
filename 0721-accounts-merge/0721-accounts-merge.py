
class UnionFind:
	def __init__(self, n):
		self.parents = {}
		for i in range(n):
			self.parents[i] = i

	def find(self, a):
		if self.parents[a] != a:
			self.parents[a] = self.find(self.parents[a])
		return self.parents[a]
	
	def union(self, a, b):
		pa, pb = self.find(a), self.find(b)
		self.parents[pa] = pb
		
	
class Solution:
	def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
		m = len(accounts)
		uf = UnionFind(m)
		emails = {}
		for i in range(m):
			for j in range(1, len(accounts[i])):
				if accounts[i][j] in emails:
					uf.union(i, emails[accounts[i][j]])
				else: emails[accounts[i][j]] = i
		
		graph = collections.defaultdict(list)
		for e in sorted(emails.keys()):
			idx = uf.find(emails[e])
			if idx not in graph: 
				graph[idx].append(accounts[idx][0])
			graph[idx].append(e)			
		return graph.values()