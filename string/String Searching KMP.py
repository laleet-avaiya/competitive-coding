# String Searching KMP
# https://www.hackerearth.com/practice/algorithms/string-algorithm/string-searching/tutorial/

'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

def lpsArray(s,arr):
    
    for i in range(1,len(s)):
        j = arr[i-1]
        
        while j>0 and s[i]!=s[j]:
            arr[j]=arr[j-1]
            
        if s[i]==s[j]:
            j += 1
            arr[i]=j
    
def main():
    s = input()
    t = input()
    arr = [0]*(len(s)+1)
    lpsArray(s,arr)
    # print(arr)
    
    j=0
    i=0
    count=0
    while i<len(t):
        if s[j] == t[i]:
            i += 1
            j += 1
        
        if j==len(s):
            count += 1
            j = arr[j - 1]
        
        elif i<len(t) and s[j] != t[i]:
            if j!=0:
                j = arr[j-1]
            else:
                i += 1
        
    print(count)
if __name__ == "__main__":
    main()
