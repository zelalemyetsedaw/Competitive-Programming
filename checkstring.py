# Enter your code here. Read input from STDIN. Print output to STDOUT


flag = False
seta = set(map(int,input().split()))
n = int(input())
for i in range(n):
    setb = set(map(int,input().split()))
    
    if setb.issubset(seta) and len(setb)< len(seta):
        flag = True
    else:
        flag = False
        print(flag)
        break;
    setb.clear()

if(flag == True):
    print(True)


