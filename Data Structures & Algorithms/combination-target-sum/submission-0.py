class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = list()

        def backtrack(i, curr, remain):
            if remain == 0:
                result.append(curr[:])
                return
            if remain < 0:
                return
            for idx in range(i, len(nums)):
                curr.append(nums[idx])
                backtrack(idx, curr, remain - nums[idx])
                curr.pop()
        backtrack(0, [], target)
        return result