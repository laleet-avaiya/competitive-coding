# Valid Passwords
# 08 Sep. 2019
# https://www.hackerearth.com/codearena/ring/ba0a114/


n = int(input())
d = {}

for i in range(n):
    s = input()

    b = list(s)
    b.reverse()
    b = "".join(b)

    if b in d:
        ans_l = len(b)
        if ans_l % 2 == 0:
            ans_c = b[ans_l//2-1]
        else:
            ans_c = b[ans_l//2]

        print(ans_l, ans_c)
        break
    else:
        d[s] = 1
