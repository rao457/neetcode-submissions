class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0
        for substr_length in range(1, n+1):
            for st_idx in range(n - substr_length + 1):
                end_idx = st_idx + substr_length - 1

                if substr_length == 1:
                    dp[st_idx][end_idx] = True
                elif substr_length == 2:
                    dp[st_idx][end_idx] = s[st_idx] == s[end_idx]
                else:
                    outer_match = s[st_idx] == s[end_idx]
                    inner_palindrome_match = dp[st_idx + 1][end_idx - 1]
                    dp[st_idx][end_idx] = (outer_match and inner_palindrome_match)
                if dp[st_idx][end_idx]:
                    count += 1
        return count