# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
k = int(input())
count = Counter(input().split())
for item in count:
    if count[item] == 1:
        print(item)
