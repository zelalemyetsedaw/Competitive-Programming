class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        dransom = defaultdict(int)
        for i in ransomNote:
            dransom[i] += 1
        dmagazine = defaultdict(int)
        for i in magazine:
            dmagazine[i] += 1
           
        for key in dransom:
            if dransom[key] > dmagazine[key]:
                return False
        return True