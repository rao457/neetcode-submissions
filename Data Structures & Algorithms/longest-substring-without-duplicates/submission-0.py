class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""
        seen = set()
        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            current = s[l: r+1]

            if len(current) > len(longest):
                longest = current

        return len(longest)