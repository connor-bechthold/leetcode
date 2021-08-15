class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = {}
        for i in range(amount + 1):
            if i in coins:
                dp[i] = 1
            else:
                x = i + 1
                for coin in coins:
                    if (i - coin) >= 0 and dp[i - coin] != 0 and dp[i - coin] < x:
                        x = dp[i - coin] + 1
                if x == (i + 1):
                    x = 0
                dp[i] = x
        if dp[amount] == 0:
            return -1
        else:
            return dp[amount]
