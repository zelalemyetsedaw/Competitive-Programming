# Enter your code here. Read input from STDIN. Print output to STDOUT

en = int(input())
english = set(input().split())
ef = int(input())
french = set(input().split())
print(len(english.union(french)))
