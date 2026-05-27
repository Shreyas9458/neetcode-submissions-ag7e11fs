class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = list()
        
        def backtrack(i, curr):
            result.append(list(curr))

            for idx in range(i, len(nums)):
                curr.append(nums[idx])
                backtrack(idx + 1, curr)
                curr.pop()
        backtrack(0, [])

        return result
        