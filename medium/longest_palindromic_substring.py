class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [([False] * (len(s))) for i in range(len(s))]
        string = ""
        for j in range(len(s)):
            for i in range(j + 1):
                if i == j:
                    dp[i][j] = True
                elif i + 1 == j:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j] and dp[i+1][j-1])
                if dp[i][j] and j - i + 1 > len(string):
                    string = s[i:j+1]
        return string
