class Solution:
    def minWindow(self, s: str, t: str) -> str:
        charCount = Counter(t)
        minWindow = (0, float("inf"))
        target = len(t)
        left = 0

        for right in range(len(s)):
            if charCount[s[right]] > 0:
                target -= 1
            charCount[s[right]] -= 1

            if target == 0:
                while True:
                    if charCount[s[left]] == 0:
                        break
                    charCount[s[left]] += 1
                    left += 1
                if right - left < minWindow[1] - minWindow[0]:
                    minWindow = (left, right)
                charCount[s[left]] += 1
                target += 1
                left += 1
        return "" if minWindow[1] > len(s) else s[minWindow[0]: minWindow[1] + 1]