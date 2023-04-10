class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        minvalue = 27
        for i in letters:
            if i > target:
                minvalue = min(minvalue,ord(i)-ord(target))
        
        if minvalue == 27:
            return letters[0]
        return chr(ord(target) + minvalue)