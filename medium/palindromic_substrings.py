class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [([False] * (len(s))) for i in range(len(s))]
        count = 0
        for j in range(len(s)):
            for i in range(j + 1):
                if i == j:
                    dp[i][j] = True
                elif i + 1 == j:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j] and dp[i+1][j-1])
                if dp[i][j]:
                    count += 1
        return count
