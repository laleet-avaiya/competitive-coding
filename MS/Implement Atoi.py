# Implement Atoi 
# 17 July 2019
# https://practice.geeksforgeeks.org/problems/implement-atoi/1

def atoi(string):
    # Code here
    try:
        return int(string)
    except:
        return -1


# Swap kth elements
# 17 July 2019
# https://practice.geeksforgeeks.org/problems/swap-kth-elements/0
#code
for _ in range(int(input())):
    n,a = map(int,input().split())
    arr = list(map(int,input().split()))
    arr[a-1],arr[n-a] = arr[n-a],arr[a-1]
    
    for i in arr:
        print(i,end=" ")
    print("")