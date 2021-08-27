class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ref = {}
        for string in strs:
            sort = "".join(sorted(string))
            if sort not in ref:
                ref[sort] = [string]
            else:
                ref[sort].append(string)
        return ref.values()
