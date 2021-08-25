class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        longest = i = j = 0
        ref = {}
        while j < len(s):
            if s[j] in ref:
                i = max(i, ref[s[j]] + 1)
            ref[s[j]] = j
            longest = max(longest, j - i + 1)
            j += 1
        return longest
