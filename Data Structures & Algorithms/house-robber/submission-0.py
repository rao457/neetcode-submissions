class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        for i in range(len(nums)):
            take = nums[i] + (dp[i - 2] if i - 2 >= 0 else 0)
            skip = dp[i - 1] if i - 1 >= 0 else 0

            dp[i] = max(take, skip)
        return dp[-1]