from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)
        for cor, pre in prerequisites:
            preMap[cor].append(pre)
        
        visited, cycle = set(), set()
        result = list()

        def dfs(cor):
            if cor in cycle:
                return False
            if cor in visited:
                return True
            cycle.add(cor)
            for pre in preMap[cor]:
                if not dfs(pre):
                    return False
            cycle.remove(cor)
            visited.add(cor)
            result.append(cor)
            return True
        
        for cor in range(numCourses):
            if not dfs(cor):
                return list()
        return result
        