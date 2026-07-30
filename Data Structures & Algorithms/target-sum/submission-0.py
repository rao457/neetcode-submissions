class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(index, curr_sum):
            if index == len(nums):
                return 1 if curr_sum == target else 0
            
            if (index, curr_sum) in memo:
                return memo[(index, curr_sum)]
            add = dfs(index + 1, curr_sum + nums[index])
            sub = dfs(index + 1, curr_sum - nums[index])

            memo[(index, curr_sum)] = add + sub
            return memo[(index, curr_sum)]
        return dfs(0, 0)