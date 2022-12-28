class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = 0
        right = 0
        mergedstring = []
        while(left<len(word1) and right<len(word2)):
            mergedstring.append(word1[left])
            left+=1
            mergedstring.append(word2[right])
            right+=1
        while(left<len(word1)):
            mergedstring.append(word1[left])
            left +=1
        while(right<len(word2)):
            mergedstring.append(word2[right])
            right += 1
            
        answer = "".join(mergedstring)
        
        return answer