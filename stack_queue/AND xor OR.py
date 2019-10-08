# AND xor OR
# 05 June 2019
# https://www.hackerrank.com/challenges/and-xor-or/problem

def andXorOr(a):
    stack = [a[0]]; 
    max_val = -1<<256
    
    for item in a[1:]:
        while stack:
            m1,m2 = item, stack[-1]
            result = ((m1 & m2) ^ (m1 | m2)) & (m1 ^ m2)
            if result > max_val:
                max_val = result
            if item < stack[-1]:
                stack.pop()
            else:
                break
        stack.append(item)
    return max_val