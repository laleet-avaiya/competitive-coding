# Save Ironman
# https://practice.geeksforgeeks.org/problems/save-ironman/0

#code
# help(str)
for _ in range(int(input())):
    s = input()
    b = s.lower()
    # print(b)
    strs = []
    for i in b:
        if ord(i)>96 and ord(i)<124 or i.isnumeric():
            strs.append(i)
    p = list(strs)
    
    ans = "YES"
    for i in range(len(p)):
        if p[i] != strs[len(p)-1-i]:
            ans = "NO"
            break
    
    print(ans)