class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        
        for item in paths:
            item = item.split(' ')
            folder = item[0]
            for i in item[1:]:
                count,item = i.split(".txt")
                d[item].append(folder+"/"+count+".txt")
        output = []       
        for key,value in d.items():
            if(len(value)>1):
                output.append(value)
                
        return output

       