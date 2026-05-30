class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = list()

        def backtrack(open, close, curr):
            if len(curr) == n*2:
                result.append(curr)
                return
            
            if open < n:
                backtrack(open + 1, close, curr + "(")
            if close < open:
                backtrack(open, close + 1, curr + ")")
        backtrack(0, 0, "")
        return result
        