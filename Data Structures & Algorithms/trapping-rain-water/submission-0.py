class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        leftMax = 0
        rightMax = 0
        result = 0

        while start < end:
            leftMax = max(leftMax, height[start])
            rightMax = max(rightMax, height[end])

            if leftMax < rightMax:
                result += leftMax - height[start]
                start += 1
            else:
                result += rightMax - height[end]
                end -= 1
        return result
        