# 16. Stock buy and sell 
# https://practice.geeksforgeeks.org/problems/stock-buy-and-sell/0


#code

def stockBuySell(price_arr,n):
    
    # Prices must be given for at least two days 
    if n==1:
        return
    
    count = 0
    
    # solution list [buy, sell]
    sol=[]
    
    # Traverse through given price list
    i=0
    while i<n:
        
        # local Minima
        while i<n-1 and price[i+1]<=price[i]:
            i += 1
        
        
        # If we reached the end, break as no further solution possible 
        if i == n - 1:
            break; 
        
        # Store the index of minima             
        buy_at_index = i
        i += 1
        
        # local Maxima
        while i<n and price[i]>=price[i-1]:
            i += 1
        
        # Store the index of maxima 
        sell_at_index = i - 1
        # i += 1
        
        sol.append([buy_at_index,sell_at_index])
        
    # print solution 
    if len(sol) == 0:
        print("No Profit")
    else:
        for i in sol:
            print("({} {})".format(i[0],i[1]),end=" ")
        print("")
      
    return; 
        
    
    
    
    
    
    
t=int(input())
while t>0:
    t=t-1
    n=int(input())
    price=list(map(int,input().split()))
    stockBuySell(price,n)