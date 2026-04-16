class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = list()
        result = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                lastIdx, lastTemp = stack.pop()
                result[lastIdx] = idx - lastIdx
            stack.append([idx, temp])
        return result 
        