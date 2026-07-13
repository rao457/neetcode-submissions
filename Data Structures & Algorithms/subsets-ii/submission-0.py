class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        curr = []

        def backtrack(index):
            ans.append(curr.copy())

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                
                curr.append(nums[i])
                backtrack(i + 1)
                curr.pop()
        backtrack(0)
        return ans