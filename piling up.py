# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())
for i in range(T):
    n = int(input())
    lists = list(map(int,input().split()))
    
    left = 0
    right = len(lists)-1
    prev = max(lists[left],lists[right])
    while left<right:
        if lists[left] > lists[right]:
            if(lists[left]<=prev):
                prev = lists[left]
                left += 1
            else:
                print("No")
                break
        else: 
            if(lists[right]<=prev):
                prev = lists[right]
                right -= 1
            else:
                print("No")
                break
    else:
        print("Yes")
                
