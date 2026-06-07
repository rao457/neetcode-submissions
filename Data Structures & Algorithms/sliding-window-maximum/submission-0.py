class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
    
        left = 0
        right = left + k
        while(right <= len(nums)):
            result.append(max(nums[left: left + k]))
            left += 1
            right += 1
        return result