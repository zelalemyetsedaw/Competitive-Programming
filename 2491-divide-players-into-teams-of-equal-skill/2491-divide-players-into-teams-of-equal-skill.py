class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        left = 0
        right = len(skill)-1
        n = len(skill)
        chemistry = 0
        
        skill.sort()
        summ = skill[left] + skill[right]
        while left < right:
            if skill[left] + skill[right] != summ:
                return -1
            chemistry += skill[left] * skill[right]
            left += 1
            right -= 1
            
        return chemistry