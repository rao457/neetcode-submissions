class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        map = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if (nums[i]) in map:
                ans.append(map.get(nums[i]))
                ans.append(i)
                return ans
            else:
                map[difference] = i
        return ans