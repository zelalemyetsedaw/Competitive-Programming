class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = str(a)
        b = str(b)
        i = len(a)-1
        j = len(b)-1
        ans = []
        summ = 0
        while i >= 0 and j >= 0:
            summ += int(a[i]) + int(b[j]) 
            if summ <= 1:
                ans.append(summ)
                summ = 0
            elif summ == 2:
                ans.append(0)
                summ = 1
            else:
                ans.append(1)
                summ = 1
            i -= 1
            j -= 1
        while i>=0:
            summ += int(a[i])
            if summ == 2:
                ans.append(0)
                summ = 1
            else:
                ans.append(summ)
                summ = 0
            i-=1
        while j>=0:
            summ += int(b[j])
            if summ == 2:
                ans.append(0)
                summ = 1
            else:
                ans.append(summ)
                summ = 0
            j -= 1
        if summ == 1:
            ans.append(1)
        ans.reverse()
        
        sol = ""
        for i in ans:
            sol += str(i)
        
        return sol
            
            