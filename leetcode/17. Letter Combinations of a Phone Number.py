'''
17. Letter Combinations of a Phone Number
2nd June 2022

Start: 7:23 PM
End  : -
Total: -

https://redquark.org/leetcode/0017-letter-combinations/
'''


class Solution:
    def findCombinations(self, combinations, digits, previous, index, lettersAndNumbersMapping):
        # Base condition to stop recursion
        if index == len(digits):
            combinations.append(previous)
            return
        # Get the letters corresponding to the current index of digits string
        letters = lettersAndNumbersMapping[int(digits[index])]
        # Loop through all the characters in the current combination of letters
        for i in range(0, len(letters)):
            self.findCombinations(combinations, digits, previous + letters[i], index + 1, lettersAndNumbersMapping)


    def letterCombinations(self, digits: str) -> List[str]:
        # Resultant list
        combinations = []
        # Base condition
        if digits is None or len(digits) == 0:
            return combinations
        # Mappings of letters and numbers
        lettersAndNumbersMapping = [
            "Anirudh",
            "is awesome",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
        ]
        self.findCombinations(combinations, digits, "", 0, lettersAndNumbersMapping)
        return combinations
