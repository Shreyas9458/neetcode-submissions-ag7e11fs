class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = list()

        def dfs(string, partition):
            if not string:
                result.append(partition[:])
                return
            
            for i in range(1, len(string) + 1):
                pre, post = string[:i], string[i:]
                if pre == pre[::-1]:
                    partition.append(pre)
                    dfs(post, partition)
                    partition.pop()
        dfs(s, [])
        return result