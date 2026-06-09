class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        num = digits[0]
        for i in range(1, len(digits)):
            num *= 10
            num += digits[i]
        num += 1
        while(num > 0):
            result.append(num % 10)
            num = num // 10
        return result[::-1]