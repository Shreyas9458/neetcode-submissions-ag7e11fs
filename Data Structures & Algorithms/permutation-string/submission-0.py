class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        left, right = 0, len(s1)

        while right <= len(s2):
            if Counter(s2[left:right]) == counter:
                return True
            else:
                left += 1
                right += 1
        return False 
        