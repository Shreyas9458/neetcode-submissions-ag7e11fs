class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        result = 0
        visited = dict()
        for right in range(len(s)):
            if s[right] in visited:
                left = max(left, visited[s[right]])
            result = max(right - left + 1, result)
            visited[s[right]] = right + 1
        return result
        