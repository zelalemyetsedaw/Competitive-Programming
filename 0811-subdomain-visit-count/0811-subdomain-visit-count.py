class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = defaultdict(int)
        
        for domain in cpdomains:
            count,d = domain.split()
            count  = int(count)
            d = d.split(".")
            for i in range(len(d)):
                counts[".".join(d[i:])] += count
                
        return [f"{count} {domain}" for domain,count in counts.items()]
        
        
        