class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = current = -100001
        for num in nums:
            
            current = max(current + num, num)
            total = max(total, current)
        
        return total
