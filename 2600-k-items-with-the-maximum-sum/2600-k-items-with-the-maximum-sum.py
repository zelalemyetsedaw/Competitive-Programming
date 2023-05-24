class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        answer = 0
        if k <= numOnes:
            answer = k
        elif k<= numOnes + numZeros:
            answer = numOnes
        else: answer = numOnes - (k-numZeros-numOnes)
            
        return answer