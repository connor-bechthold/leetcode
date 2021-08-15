class Solution:
    def climbStairs(self, n: int, memo = {}) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n in memo:
            return memo[n]
        else:
            x = self.climbStairs(n-2, memo) + self.climbStairs(n-1, memo)
            memo[n] = x
            return x
