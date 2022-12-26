# Enter your code here. Read input from STDIN. Print output to STDOUT

numOfEnglish = int(input())
english = set(input().split())
numOfFrench = int(input())
french = set(input().split())
print(len(english.union(french)))
