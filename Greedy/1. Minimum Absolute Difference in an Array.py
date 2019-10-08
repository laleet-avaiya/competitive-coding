# Minimum Absolute Difference in an Array
# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem


def minimumAbsoluteDifference(arr):
    
    arr.sort()
    minimum=999999999

    for i in range(len(arr)-1):
        if minimum> abs(arr[i]-arr[i+1]):
            minimum = abs(arr[i]-arr[i+1])
        
    return (minimum)