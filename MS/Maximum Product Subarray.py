# Maximum Product Subarray 
# 19 July 2019
# https://practice.geeksforgeeks.org/problems/maximum-product-subarray/0


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    # print(arr)
    
    current_max_till_index = arr[0]
    global_max = arr[0]
    current_min_till_index = arr[0]
    
    arr.pop(0)
    for i in arr:
        
        temp = current_max_till_index
        
        current_max_till_index = max(i,max(current_min_till_index*i,temp*i))
        
        global_max = max(global_max,current_max_till_index)
        
        current_min_till_index = min(i,min(current_min_till_index*i,temp*i))
    
    print(global_max)