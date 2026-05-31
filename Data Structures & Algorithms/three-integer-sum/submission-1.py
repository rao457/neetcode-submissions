class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            start = i + 1
            end = len(nums) - 1
            
            while(start < end):
                curr_result = []
                target = nums[i] + nums[start] + nums[end]
                if (target > 0):
                    end -= 1
                elif (target < 0):
                    start += 1
                else:
                    curr_result.append(nums[i])
                    curr_result.append(nums[start])
                    start += 1
                    curr_result.append(nums[end])
                    end -= 1
                    result.append(curr_result)
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
                    continue
        return result
