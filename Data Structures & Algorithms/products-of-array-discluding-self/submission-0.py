class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        prefix = 1

        for i in range(1, len(nums)):
            result[i] = nums[i - 1] * prefix
            prefix *= nums[i-1]
        print(result)

        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result
        
        