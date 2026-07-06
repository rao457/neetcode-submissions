class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        palindromic_table = [[False] * n for _ in range(n)]
        longest = ""

        for substring_length in range(1, n + 1):

            for start_index in range(n - substring_length + 1):
                end_index = start_index + substring_length - 1

                if substring_length == 1:
                    palindromic_table[start_index][end_index] = True
                elif substring_length == 2:
                    palindromic_table[start_index][end_index] = (s[start_index] == s[end_index])
                else:
                    outer_match_chars = s[start_index] == s[end_index]
                    inner_palindrome = palindromic_table[start_index+1][end_index - 1]

                    palindromic_table[start_index][end_index] = (outer_match_chars and inner_palindrome)

                if (palindromic_table[start_index][end_index] and substring_length > len(longest)):
                    longest = s[start_index:end_index + 1]
        return longest