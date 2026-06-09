class Solution:
    def squareSum(self, num: int) -> int:
        sum = 0
        while (num > 0):
            rem = num % 10
            sum += (rem**2)
            num = num // 10
        return sum

    def isHappy(self, n: int) -> bool:
        seen = set()
        while (n != 1):
            n = self.squareSum(n)
            if n in seen:
                return False
            seen.add(n)
        return True