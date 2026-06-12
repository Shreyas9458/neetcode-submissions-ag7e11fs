class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i: list() for i in range(numCourses)}
        for cor, pre in prerequisites:
            preMap[cor].append(pre)
        visitedSet = set()

        def dfs(cor):
            if cor in visitedSet:
                return False
            if not preMap[cor]:
                return True
            visitedSet.add(cor)

            for pre in preMap[cor]:
                if not dfs(pre):
                    return False
            visitedSet.remove(cor)
            preMap[cor] = []
            return True 
        
        for cor in range(numCourses):
            if not dfs(cor):
                return False
        return True
        