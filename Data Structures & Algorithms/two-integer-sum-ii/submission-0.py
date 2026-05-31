class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        start = 0
        end = len(numbers) - 1
        while(start < end):
            if (numbers[start] + numbers[end] < target):
                start += 1
            elif (numbers[start] + numbers[end] > target):
                end -= 1
            else:
                result.append(start+1)
                result.append(end+1)
                break
            
        return result