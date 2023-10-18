class Solution:
    def countVowels(self, word: str) -> int:
        
        dp = []
        for i, el in enumerate(word):
            if el in 'aeiou':
                running_sum = i + 1 + (dp[-1] if dp else 0)
                dp.append(running_sum)
            else:
                dp.append(dp[-1] if dp else 0)
        return sum(dp)