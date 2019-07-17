# Day of the week 
# 17 July 2019
# https://practice.geeksforgeeks.org/problems/day-of-the-week/0

import calendar

t=int(input())
for i in range(t):
    d,m,y=map(int,input().split())
    s=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    a=calendar.weekday(y,m,d)
    print(s[a])
    