class Solution:
    def myPow(self, x: float, n: int) -> float:
        BF = n
        if n < 0:
            x = 1/x
            BF = -BF
        ans = 1
        
        while (BF > 0):
            if (BF %2 == 1):
                ans *= x
            x *= x
            BF //= 2
        return ans