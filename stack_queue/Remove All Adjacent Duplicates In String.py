# *Remove All Adjacent Duplicates In String*

def removeDuplicates(s):
    s=list(s)
    a=[]
    prev = ""
    for i in s:
        if len(a)==0:
            if prev!=i:
                a.append(i)
        elif a[-1]==i:
            prev = a.pop()
        else:
            if prev!=i:
                a.append(i)
    print("".join(a))

removeDuplicates("AAAAACCAAAAAAAAABCCB");

