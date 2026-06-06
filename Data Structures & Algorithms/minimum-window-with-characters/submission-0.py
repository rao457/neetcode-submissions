class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_window = ""
        window = {}
        left = 0
        need = {}
        for i in t:
            need[i] = need.get(i, 0) + 1
        required = 0
        for i in need.keys():
            required += 1
        min_start = 0
        min_end = 0
        min_length = float('inf')

        formed = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0) + 1
            if s[r] in need and  window[s[r]] == need[s[r]]:
                formed += 1
            while(formed == required):
                if (r - left + 1) < min_length:
                    min_length = r - left + 1
                    min_start = left 
                    
                
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    formed -= 1
                
                left += 1

        if min_length == float('inf'):
            return ""
        else:
            return s[min_start: min_start + min_length]
        