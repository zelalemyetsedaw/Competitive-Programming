# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n,m = map(int,input().split())
d = defaultdict(list)

for i in range(1,n+1):
    v = input()
    d[v].append(i)
    
for i in range(m):
    k = input()
    if k in d:
        print(*d[k],sep = " ")
    else:
        print(-1)
