class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        result = float('inf')
        while left <= right:
            m = left + (right - left) // 2

            if nums[left] <= nums[m]:
                result = min(nums[left], result)
                left = m + 1
            else:
                result = min(nums[m], result)
                right = m - 1
        return result

        