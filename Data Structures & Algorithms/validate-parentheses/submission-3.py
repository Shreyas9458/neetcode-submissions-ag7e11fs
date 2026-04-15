class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for i in s:
            if i in "[{(":
                stack.append(i)
            else:
                if stack and stack[-1] + i in "{}()[]":
                    stack.pop()
                elif stack and stack[-1] + i not in "{}[]()":
                    return False
                elif not stack:
                    return False
        return not stack