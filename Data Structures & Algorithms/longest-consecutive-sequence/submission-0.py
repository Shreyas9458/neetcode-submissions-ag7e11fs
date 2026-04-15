class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        largestSeq = 0

        for i in nums:
            if i - 1 not in numSet:
                val = i + 1
                while val in numSet:
                    val += 1
                largestSeq = max(val - i, largestSeq)
        return largestSeq
        