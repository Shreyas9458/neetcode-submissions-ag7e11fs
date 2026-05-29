class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = list()
        candidates.sort()

        def backtrack(i, curr, remain):
            if remain == 0:
                result.append(curr[:])
                return
            
            for idx in range(i, len(candidates)):
                if idx > i and candidates[idx] == candidates[idx - 1]:
                    continue
                
                if candidates[idx] > remain:
                    break
                curr.append(candidates[idx])
                backtrack(idx + 1, curr, remain - candidates[idx])
                curr.pop()
        backtrack(0, [], target)
        return result
        