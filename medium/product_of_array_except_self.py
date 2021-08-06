class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        
        front = 1
        for i in range(1, len(nums)):
            front *= nums[i - 1]
            output[i] *= front
            
        back = 1
        for i in range(len(nums) - 2, -1, -1):
            back *= nums[i + 1]
            output[i] *= back
            
        return output
