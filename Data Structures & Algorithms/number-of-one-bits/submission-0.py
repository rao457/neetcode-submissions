class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            mask = 1 << i
            if mask & n != 0:
                count += 1
        return count