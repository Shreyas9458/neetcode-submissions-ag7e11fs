class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        result = list()

        for i in range(k, len(nums) + 1):
            # print(nums[i-k: i])
            result.append(max(nums[i-k: i]))
        return result
        