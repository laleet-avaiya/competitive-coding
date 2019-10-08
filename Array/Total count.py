# Total count
# 08 Sep. 2019
# https://practice.geeksforgeeks.org/problems/total-count/0/?ref=self

if __name__ == "__main__":

    test_cases = int(input())

    for test in range(test_cases):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))

        ans = 0

        for i in arr:
            if i % k == 0:
                ans += i//k
            else:
                ans += i//k + 1

        print(ans)
