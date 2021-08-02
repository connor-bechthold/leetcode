class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charMap = {}
        for char in s:
            if char in charMap:
                charMap[char] += 1
            else:
                charMap[char] = 1
        for char in t:
            if char not in charMap:
                return False
            else:
                charMap[char] -= 1
                if charMap[char] < 0:
                    return False
        return True
