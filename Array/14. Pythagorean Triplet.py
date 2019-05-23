# 14. Pythagorean Triplet 
# https://practice.geeksforgeeks.org/problems/pythagorean-triplet/0
# Time complexity of this method is O(n2).


#code

# Returns true if there is Pythagorean 
# triplet in ar[0..n-1] 
def isTriplet(ar, n): 
    # Square all the elemennts 
    for i in range(n): 
        ar[i] = ar[i] * ar[i] 
  
    # sort array elements 
    ar.sort() 
  
    # fix one element 
    # and find other two 
    # i goes from n - 1 to 2 
    for i in range(n-1, 1, -1): 
        # start two index variables from  
        # two corners of the array and  
        # move them toward each other 
        j = 0
        k = i - 1
        while (j < k): 
            # A triplet found 
            if (ar[j] + ar[k] == ar[i]): 
                return True
            else: 
                if (ar[j] + ar[k] < ar[i]): 
                    j = j + 1
                else: 
                    k = k - 1
    # If we reach here, then no triplet found 
    return False
  

t=int(input())
while t>0:
    t=t-1
    n=int(input())
    a=list(map(int,input().split()))
    
    if(isTriplet(a, n)): 
        print("Yes") 
    else: 
        print("No") 