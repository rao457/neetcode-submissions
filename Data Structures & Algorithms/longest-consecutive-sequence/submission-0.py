class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0  # Track the absolute maximum here
        nums_set = set(nums)
        
        for i in nums_set:
            if not i - 1 in nums_set:
                count = 1
                current = i
                while (current + 1) in nums_set:
                    count += 1
                    current += 1
                
                # Keep the largest streak found so far
                longest = max(longest, count)
                
        return longest
