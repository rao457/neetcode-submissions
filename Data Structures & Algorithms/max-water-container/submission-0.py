class Solution:
    def maxArea(self, nums: List[int]) -> int:
        
        max_water = -1
        start = 0
        end = len(nums) - 1
        while(start < end):
            height = min(nums[start], nums[end])
            width = end - start
            curr_water = height * width
            max_water = max(curr_water, max_water)
            if (nums[start] < nums[end]):
                start += 1
            else:
                end -= 1
        return max_water
