class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        counter = [0] * 26
        left = 0

        for right in range(len(s)):
            counter[ord(s[right]) - ord('A')] += 1
            while (right - left + 1) - max(counter) > k:
                counter[ord(s[left]) - ord('A')] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest        