class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = defaultdict(int)
        for index,value in enumerate(order):
            d[value] = index
        before = words[0]
        flag = True
        for item in words[1:]:
            x = min(len(item),len(before))
            if(before[0:x]==item[0:x]):
                if len(item) >= len(before):
                    flag= True
                else:
                    flag = False
            else:
                for i in range(x):
                    if(d[item[i]] == d[before[i]]):
                        flag = True
                    elif d[item[i]] > d[before[i]]:
                        flag = True
                    else:
                        flag = False
                    if(d[item[i]]!=d[before[i]]):
                        break
            before = item
            if(flag==False):
                break
            
            
         
        return flag 
            
            