class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        n = len(skill) -1
        l = 0
        r = len(skill)-1
        chem =0
        summ = 0
        while(l < r):
            summ = skill[l] + skill[r]
            if summ == (skill[0] + skill[n]):
                chem += skill[l] * skill[r]
            else:
                return -1
            l += 1
            r -=1
            
        return chem
                