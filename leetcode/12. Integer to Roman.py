'''
12. Integer to Roman
2nd June 2022

Start: 6:52 PM
End  : 7:18 PM
Total: 26 Min

Laleet Avaiya
'''

class Solution:
    def intToRoman(self, num: int) -> str:
        M = ["", "M", "MM", "MMM", "MMMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        
        return M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) // 10] + I[num % 10]