class UnionFind:
    def __init__(self):
        self.parent = [chr(ord('a')+i)for i in range(26)]

    def find(self, char):
        return self.parent[ord(char)-ord('a')]

    def union(self, char1: str, char2: str):
        if self.find(char1) > self.find(char2):
            char1, char2 = char2, char1

        if self.find(char1) != self.find(char2):
            oldParent = self.find(char2)
            newParent = self.find(char1)

            for i in range(26):
                if self.parent[i] == oldParent:
                    self.parent[i] = newParent

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        unionFind = UnionFind()
        ans = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                unionFind.union(s1[i], s2[i])

        for c in baseStr:
            ans.append(unionFind.find(c))

        return "".join(ans)