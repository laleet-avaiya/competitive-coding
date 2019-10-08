# Reverse each word in a given string
# 08 Sep. 2019
# https://practice.geeksforgeeks.org/problems/reverse-each-word-in-a-given-string/0/?ref=self


if __name__ == "__main__":
    for _ in range(int(input())):
        s = list(input().split("."))

        for j in range(len(s)):
            st = list(s[j])
            st.reverse()
            s[j] = "".join(st)

        print(".".join(s))
