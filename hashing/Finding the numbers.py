# Finding the numbers
# 08 Sep. 2019
# https://practice.geeksforgeeks.org/problems/finding-the-numbers/0/?ref=self

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))

        dictionary = {}

        for i in arr:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1

        ans = []

        for i in dictionary:
            if dictionary[i] % 2 != 0:
                ans.append(i)

        ans.sort()

        for i in ans:
            print(i, end=" ")

        print("")
