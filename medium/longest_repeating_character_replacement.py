class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = j = 0
        longest = maxChars = 0
        charCount = {}
        while j < len(s):
            if s[j] in charCount:
                charCount[s[j]] += 1
            else:
                charCount[s[j]] = 1
            maxChars = max(maxChars, charCount[s[j]])
            while j - i - maxChars + 1 > k:
                charCount[s[i]] -= 1
                i += 1
            
            longest = max(longest, j - i + 1)
            
            j += 1
            
        return longest
