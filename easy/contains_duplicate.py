class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lookup = set()
        for num in nums:
            if num in lookup:
                return True
            else:
                lookup.add(num)
        
        return False
