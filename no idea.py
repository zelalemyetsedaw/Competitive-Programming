# Enter your code here. Read input from STDIN. Print output to STDOUT

n,m = map(int,input().split())
lists = input().split()
a = set(input().split())
b = set(input().split())
happiness = 0

for item in lists:
    if item in a:
        happiness +=1
    elif item in b:
        happiness -=1
        
        
print(happiness)

