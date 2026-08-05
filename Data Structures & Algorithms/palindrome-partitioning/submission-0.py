class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        part = []

        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        def backtrack(start):
            if start == len(s):
                ans.append(part[:])
                return
            
            for end in range(start, len(s)):
                if isPalindrome(start, end):
                    part.append(s[start:end+1])
                    backtrack(end+1)
                    part.pop()
        backtrack(0)
        return ans