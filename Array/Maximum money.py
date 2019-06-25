# Maximum money
# 17 June 2019
# https://practice.geeksforgeeks.org/problems/maximum-money/0

#code

for _ in range(int(input())):
    p= list(map(int,input().split()))
    with_ = 0
    without = 0
    arr = [p[1]]*p[0]
    
    for i in arr:
        temp = with_
        
        with_ = without + i
        without = temp
        
        # with_,without = without,with_
    
    print(max(with_,without))