# Find Maximum Index Product
# https://www.hackerrank.com/challenges/find-maximum-index-product/problem

def solve(arr):
    n = len(arr)
    left = [0]*n
    right = [0]*n
    
    left[0]=0
    right[n-1]=0

    stack = [0]

    for i in range(1,n):
            # if arr[s.peek()] > arr[i]
            if arr[stack[-1]] > arr[i]:
                left[i]=stack[-1]+1
                stack.append(i)
            else:
                while len(stack)>0 and arr[stack[-1]-1] <= arr[i]:
                    stack.pop()
                if len(stack)==0:
                    stack.append(i+1)
                    left[i]=0
                elif arr[i] <= arr[stack[-1]-1]:
                    left[i]=stack[-1]
                    stack.append(i+1)


    stack = [n-1]
    for i in range(n-2,-1,-1):
        if arr[stack[-1]] > arr[i]:
            right[i]=i+2
            stack.append(i)
        else:
            while len(stack)>0 and arr[stack[-1]-1] <= arr[i]:
                stack.pop()
            if len(stack)==0:
                stack.append(i+1)
                right[i]=0
            elif arr[i] <= arr[stack[-1]-1]:
                right[i]=stack[-1]
                stack.append(i+1)



    temp = 0
    for i in range(n):
        ans = (left[i])*(right[i])
        if ans >temp:
            temp =ans
   
    return temp
