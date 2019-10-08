# Cross character
# 08 Sep. 2019
# https://practice.geeksforgeeks.org/problems/cross-character/0/?ref=self


if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()

        mat = [[' ' for i in range(len(s))]for j in range(len(s))]

        for i in range(len(s)):
            mat[i][i] = s[i]

        j = 0
        for i in range(len(s)-1, -1, -1):
            mat[j][i] = s[i]
            j += 1

        for k in mat:
            print("".join(k), end="")

        print("")
