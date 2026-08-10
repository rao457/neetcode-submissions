class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz"
        }
        result = []
        if len(digits) == 0:
            return result
        def backtrack(index, current):
            if index == len(digits):
                result.append(current)
                return
            
            for letter in mapping[digits[index]]:
                current += letter
                backtrack(index+1, current)
                current = current[:-1]
        backtrack(0, "")
        return result