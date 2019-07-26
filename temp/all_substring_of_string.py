def findLength(string):  
  
    n = len(string)  
    maxlen = 0 # Initialize result  

    Sum = [[0 for x in range(n)]for y in range(n)] 
  
    for i in range(0, n):  
        Sum[i][i] = int(string[i])  
 
    for length in range(2, n + 1):  
        for i in range(0, n + 1 - length):  
          
            j = i + length - 1
            k = length // 2
  
            Sum[i][j] = (Sum[i][j - k] + Sum[j - k + 1][j])
      
            if (length % 2 == 0 and Sum[i][j - length // 2] == Sum[(i+length//2)][j] and length > maxlen): 
                maxlen = length
            
    return maxlen  

# Driver Code 
if __name__ == "__main__": 
  
    string = "123123"
    print("Length of the substring is", findLength(string))      
