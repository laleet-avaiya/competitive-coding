# Sum of primes
# 08 Sep. 2019
# https://practice.geeksforgeeks.org/problems/sum-of-primes/0/?ref=self

if __name__ == "__main__":

    for _ in range(int(input())):
        n = int(input())
        ans = 0
        while n != 0:
            a = n % 10
            if a in [2, 3, 5, 7]:
                ans += a
            n = n//10

        print(ans)
