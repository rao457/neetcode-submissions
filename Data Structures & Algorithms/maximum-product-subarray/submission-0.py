class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        prev_max = nums[0]
        prev_min = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            curr_max = max(num, num*prev_max, num*prev_min)
            curr_min = min(num, num * prev_max, num * prev_min)

            prev_max = curr_max
            prev_min = curr_min

            ans = max(ans, curr_max)
        return ans